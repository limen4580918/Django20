"""
因为在django中只支持
"""

from pymysql import install_as_MySQLdb

"""After this function is called, any application that imports MySQLdb or
 _mysql will unwittingly actually use pymysql."""
# 调用这个函数后,任何导入MySQLdb或者_mysql的应用实际都将默认导入pymysql,而不是MySQLdb
install_as_MySQLdb()


# 下面这两行代码与上面的两行等价
# import pymysql
# pymysql.install_as_MySQLdb()