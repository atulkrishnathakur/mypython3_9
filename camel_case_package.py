# install pip for python 3.9 if not installed
# check version usint "$ pip3.9 --version"
# if pip installed for python3.9 then run "pip3.9 install camelcase"

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

