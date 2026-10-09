#!/usr/bin/env ruby
require 'yaml'
require 'json'
require 'base64'
require 'open3'
require 'digest'
ROOT = File.expand_path('..', __dir__)
REGISTRY = File.join(ROOT, 'canon/synchronization.yaml')
def gh(*args, input: nil)
  stdout, stderr, status = Open3.capture3('gh', *args, stdin_data: input.to_s)
  raise "gh #{args.join(' ')} failed: #{stderr.strip}" unless status.success?
  stdout
end
records = YAML.load_file(REGISTRY).fetch('artifacts')
errors = []
changed = 0
checked = 0
records.each do |name, artifact|
  canonical_path = artifact.fetch('hq_markdown')
  begin
    remote = JSON.parse(gh('api', "repos/XLR8ROS/xlr8ros-hq/contents/#{canonical_path}", '-H', 'Accept: application/vnd.github+json'))
    expected = Base64.decode64(remote.fetch('content'))
    unless File.binread(File.join(ROOT, canonical_path)) == expected
      raise "HQ local rendering differs from current GitHub remote: #{canonical_path}; update local checkout first"
    end
    artifact.fetch('downstream', []).each do |dest|
      repo = dest.fetch('repository'); path = dest.fetch('path')
      begin
        current = JSON.parse(gh('api', "repos/#{repo}/contents/#{path}", '-H', 'Accept: application/vnd.github+json'))
        actual = Base64.decode64(current.fetch('content'))
        checked += 1
        next if actual == expected
        payload = {'message'=>"mirror: synchronize #{name} from HQ authoritative rendering",'content'=>Base64.strict_encode64(expected),'sha'=>current.fetch('sha'),'branch'=>'main'}
        gh('api', '-X', 'PUT', "repos/#{repo}/contents/#{path}", '--input', '-', input: JSON.generate(payload))
        verified = JSON.parse(gh('api', "repos/#{repo}/contents/#{path}"))
        raise "post-write verification failed #{repo}/#{path}" unless Base64.decode64(verified.fetch('content')) == expected
        changed += 1
      rescue => e
        errors << "#{repo}/#{path}: #{e.message}"
      end
    end
  rescue => e
    errors << "#{name}: #{e.message}"
  end
end
puts JSON.generate({'checked'=>checked,'changed'=>changed,'errors'=>errors,'timestamp'=>Time.now.utc.to_s})
exit(errors.empty? ? 0 : 1)
