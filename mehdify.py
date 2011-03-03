def mehdify(status):
  replace_dict = { 'awesome': 'awesome/terrible',
                   'terrible': 'awesome/terrible',
                   'best': 'best/worst',
                   'worst': 'best/worst',
                   'better': 'better/worse',   
                   'worse': 'better/worse',
                   'love': 'love/hate',
                   'hate': 'love/hate'}

  # replace some adjectives
  words = status.split(' ')
  for word in words:
    if word in replace_dict:
      status = status.replace(word, replace_dict[word])

  # add ", bro" to @replies
  if status[0] is '@':
    return re.sub(r'[?!,.]*$', ', bro', status)

  # prepend "aww yeah" or "whoa" to some tweets
  if random.random() > 0.5:
    return 'aww yeah, ' + status

  return 'whoa, ' + status
