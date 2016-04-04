# -*- coding: utf-8 -*-. 

import unittest

from testAccions                import *
from testActorsUserHistory      import *
from testBackLog                import *
from testCategory               import *
from testHistory                import *
from testLogin                  import *
from testObjective              import *
from testObjectivesUserHistory  import *
from testRole                   import *
from testTask                   import *
from testUser                   import *
from testTeam					import *
from testArchivo                import *
from testUserHistory 			import *
from testPrecedence				import *

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = unittest.TestSuite()
    runner.run (test_suite)