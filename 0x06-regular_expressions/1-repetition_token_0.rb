#!/usr/bin/env ruby
input = ARGV[0]

regex = /hb{1,5}tn/
match = input.match(regex)

if match
  puts "#{match[0]}"
else
  puts ""
end
