input = ARGV[0]
regex = /School/
match = input.match(regex)

# Output the matched word
if match
  puts "#{match[0]}"
else
  puts ""
end
