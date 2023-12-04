import xml.dom.minidom 


treeDom = xml.dom.minidom.parse('data.xml')
root = treeDom.documentElement
# print(root)
# facts = root.getElementsByTagName('fact')
# for fact in facts:
#     if fact.hasAttribute("driver"):
#         print("Fact: " + fact.getAttribute('driver'))

for childnode in root.childNodes:
   if childnode.hasChildNodes():
      print(childnode.tagName, end=" :" )      
      print(childnode.childNodes[0].data.strip())
      if childnode.tagName == 'fact':
         try:
            # childnode.removeAttribute('driver')
            childnode.setAttribute('driver', 'like')
            treeDom.writexml(open('data.xml', 'w')) # must be a writer object with method of writing, not a file alone
        #  treeDom.writexml('data.xml')
         except xml.dom.NotFoundErr:
            print("not found")
      for grandson in childnode.childNodes:
         if grandson.hasChildNodes():
            print("---",grandson.tagName, end=' :')
            print(grandson.childNodes[0].data.strip())


   
