#!/usr/bin/env ruby
input = ARGV[0]
regex = /School/
match = input.match(regex)
if match
  puts "#{match[0]}"
else
  puts ""
end
