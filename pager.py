# Pager for PyScript!
def pager(obj, title="", line_len=36, lines_per=10):
    """Returns false if user interrupted, true if user fully readen"""
    length_of = int(int(line_len - len(title)) / 2)
    print("="*length_of + title + "="*length_of)
    print("Keyboard shortcuts:\n- Enter: Next page\n- Ctrl-C or 'q and Enter': Exit\n")
    lines = obj.split("\n")
    final = []
    readable = []
    for line in lines:
        counts = 0
        buffer = "\n"
        for letter in line:
            buffer += letter
            if counts == line_len:
                final.append(buffer)
                buffer = "-"
                counts = 1
                continue
            counts += 1
            
        final.append(buffer) if buffer != "... " else None
    count = 1
    buf = []
    for optimized_line in final:
       buf.append(optimized_line)
       if count == lines_per:
           readable.append(buf)
           buf = []
           count = 1
           continue 
       count += 1
    readable.append(buf) if buf else None
    total = len(readable)
    current_page = 1
    for items in readable:
        try:
            print("\n".join(items))
            if current_page == total:
                 print(f"<END (Page {current_page} of {total})>")
                 break
            (1 / 0) if input(f"<Page {current_page} of {total}> ").lower().strip().rstrip() == 'q' else None
            current_page += 1
        except (KeyboardInterrupt, ZeroDivisionError):
            print("Interrupted by user, exiting ...")
            return False
    print("Exiting ...")
    return True
def activate():
    import pydoc
    pydoc.saved_pager = pydoc.pager
    pydoc.pager = pager
def deactivate():
    import pydoc
    pydoc.pager = pydoc.saved_pager
    del pydoc.saved_pager
def toggle():
    try:
        deactivate()
    except:
         activate()
