"""
### A simple API handles worker & main thread communication in PyScript
How to use?
1. On main.py and worker.py, load up m2w.py
  * m2w loading tip:
    import pyscript
    data = await pyscript.fetch("https://raw.githubusercontent.com/Ericwasepic127/Ericwasepic127/refs/heads/main/m2w.py")
    with open("m2w.py", "w") as file:
        if data.ok:
           file.write(await data.text())
2. After load, import it
  * Import just as `import m2w`
3. If it's on ...
  - Main, then use
    `connect = m2w.Main() # you can pass id parameter as worker id (like #worker)`
  - Worker, then use
    `connect = m2w.Worker()`
  - If you want Tab to Tab communication, then use
    `connect = m2w.Tab() # you can add id parameter for another broadcasting channel`
  - If you want filtered Tab to Tab communication, then use
    `connect = m2w.specTab('name_to_give') # you can id parameter for another broadcasting channel`
4. Send messages using `connect.sendmsg(Message_here)` and recieve using `connect.getmsg`
"""
import js, time, warnings
from pyodide.ffi import create_proxy, to_js

class Main:
    """Main thread only, it will crash in Worker"""
    def __init__(self, id='script[type="py"][terminal]', wait=True):
      obj = js.document.querySelector(id)
      if wait:
         while not hasattr(obj, "xworker"):
             time.sleep(.1)
      self.worker = obj.xworker
      self.sendmsg = lambda msg: self.worker.postMessage(to_js(msg))
      self.getmsg = None
      self.msgs = []
      self.id = id
      self.defaultHandler()
        
    def giveDOM(self):
         """Gives DOM control"""
         warnings.warn("giveDOM() isn't working and it's not maintained, so please do not care when it doesn't works\nAlso you can clone or copy this m2w and build working solution if you want!", DeprecationWarning, stacklevel=2)
         def func(event):
          return [js.window, js.document, js.self]
         self.worker.sync.dom = create_proxy(func)
     
    def handler(self, onmessage):
      """When message received, change handler to given function (Message will given to function's first argument)"""
      def on_message(event):
       if hasattr(event.data, "to_py"):
         data = event.data.to_py()
       else:
         data = event.data
       onmessage(data)
      self.worker.onmessage = create_proxy(on_message)
    def defaultHandler(self):
     """When you modified handler, this makes onto default one"""
     def on_message(event):
          if hasattr(event.data, "to_py"):
              self.getmsg = event.data.to_py()
              self.msgs.append(event.data.to_py())
          else:
              self.getmsg = event.data
              self.msgs.append(event.data)
     self.worker.onmessage = create_proxy(on_message)

class Worker:
  """Worker thread only, it will fail on Main"""
  def __init__(self):
      self.worker = js.self
      self.sendmsg = lambda msg: self.worker.postMessage(to_js(msg))
      self.getmsg = None
      self.msgs = []
      self.defaultHandler()
      
  def handler(self, onmessage):
    """When message received, change handler to given function (Message will given to function's first argument)"""
    def on_message(event):
     if hasattr(event.data, "to_py"):
         data = event.data.to_py()
     else:
         data = event.data
     onmessage(data)
    self.worker.onmessage = create_proxy(on_message)
  def defaultHandler(self):
    """When you modified handler, this makes onto default one"""
    def on_message(event):
          if hasattr(event.data, "to_py"):
              self.getmsg = event.data.to_py()
              self.msgs.append(event.data.to_py())
          else:
              self.getmsg = event.data
              self.msgs.append(event.data)
    self.worker.onmessage = create_proxy(on_message)
  def getDOM(self):
   """Gets DOM from main thread (you need to do connect.giveDOM() at main)"""
   warnings.warn("getDOM() isn't working and it's not maintained, so please do not care when it doesn't works\nAlso you can clone or copy this m2w and build working solution if you want!", DeprecationWarning, stacklevel=2)
   from pyscript import sync
   obj = sync.dom()
   js.window = obj[0]
   js.document = obj[1]
   js.mainSelf = obj[2]

class Tab:
    """Tab to Tab connection"""
    def __init__(self, id="pythonChannel"):
        if not id:
            raise Exception("Please give a ID")
        self.worker = js.BroadcastChannel.new(id)
        self.sendmsg = lambda msg: self.worker.postMessage(to_js(msg))
        self.getmsg = None
        self.msgs = []
        self.id = id
        self.defaultHandler()
    
    def handler(self, onmessage):
        """When message received, change handler to given function (Message will given to function's first argument)"""
        def on_message(event):
            onmessage(event.data.to_py() if hasattr(event.data, "to_py") else event.data)
        self.worker.onmessage = create_proxy(on_message)
    def defaultHandler(self):
        """When you modified handler, this makes onto default one"""
        def on_message(event):
            data = event.data.to_py() if hasattr(event.data, "to_py") else event.data
            self.getmsg = data
            self.msgs.append(data)
        self.worker.onmessage = create_proxy(on_message)
    def sendTab(self, name, value):
        """Specifically sends value to 'name'-d Tab"""
        self.sendmsg({"tabName": name, "content": value})

class specTab(Tab):
    """Targets specific named Tab"""
    def __init__(self, name, id="pythonChannel"):
        self.name = name
        self.worker = js.BroadcastChannel.new(id)
        self.sendmsg = lambda msg: self.worker.postMessage(to_js(msg))
        self.getmsg = None
        self.msgs = []
        self.id = id
        self.defaultHandler()

    def handler(self, onmessage):
        """When message received, change handler to given function (Message will given to function's first argument)"""
        def on_message(event):
            data = event.data.to_py() if hasattr(event.data, "to_py") else event.data
            if not (type(data) == dict):
                self.getmsg = data 
                self.msgs.append(data)
                return
            else:
                if not (data.get("tabName") == self.name):
                    self.getmsg = data.get("content", data)
                    self.msgs.append(data.get("content", data))
                    return
                data = data.get("content", data)
                onmessage(data)
        self.worker.onmessage = create_proxy(on_message)
 
    def defaultHandler(self):
        """When you modified handler, this makes onto default one"""
        def on_message(event):
            data = event.data.to_py() if hasattr(event.data, "to_py") else event.data
            if not (type(data) == dict):
                self.getmsg = data
                self.msgs.append(data)
                return
            else:
                if not (data.get("tabName") == self.name):
                    self.getmsg = data.get("content", data)
                    self.msgs.append(data.get("content", data))
                    return
                data = data.get("content", data)
            self.getmsg = data
            self.msgs.append(data)
        self.worker.onmessage = create_proxy(on_message)
        
