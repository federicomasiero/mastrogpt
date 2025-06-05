def reverse(args):
  inp = args.get("input", "")
  out = "Please, write something."
  if inp != "":
    out = inp[::-1]
  return { "output": out }
