
known = [ 0 ]
i = 1
consecutive_success = 0
 
while True:
  if i - 6 in known or i - 9 in known or i - 20 in known:
    known.append(i)
    consecutive_success += 1
    if consecutive_success == 6:
      print "All numbers >=  %d are mcnugget" % (i - 5)
      break
  else:
    print i
    consecutive_success = 0
  i += 1

  