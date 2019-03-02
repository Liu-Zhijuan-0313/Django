"""
引入数据库驱动
(在根模块的__init__.py中引入，并做伪装，pymysql伪装为MySQLdb）
"""

import pymysql
pymysql.install_as_MySQLdb()
