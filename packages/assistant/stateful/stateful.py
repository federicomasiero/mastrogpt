import chat
import history

def stateful(args):
  
  inp = args.get("input", "")
  out = f"Hello from {chat.MODEL}"
  res = {}
  
  if inp != "":
    # load the history in the chat
    ch = chat.Chat(args)
    hi = history.History(args)
    hi.load(ch)
    # add a message and save it 
    msg = f"user:{inp}"
    ch.add(msg)
    print(ch.messages)
    out = ch.complete()
    # complete, save the assistant and return the id
    hi.save(msg)
    hi.save(f"assistant:{out}")
    res["state"] = hi.id()

  res['output'] = out
  return res
