#!/usr/bin/env ruby
# Get the argument from the command line
input = ARGV[0]

# Define the regular expression
regex = /School/
match = input.match(regex)

if match
  puts "#{match[0]}"
else
  puts ""
end
