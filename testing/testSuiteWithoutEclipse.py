# -*- coding: utf-8 -*-.

import os
import unittest

os.chdir("testing")

#from testAcceptanceCriteria     import *
from testAccions                import *
from testActorsUserHistory      import *
from testArchivo                import *
from testBackLog                import *
from testCategory               import *
from testElementMeeting			import *
from testHistory                import *
from testLogin                  import *
from testMeeting 				import *
from testObjective              import *
from testObjectivesUserHistory  import *
from testPrecedence             import *
from testPrueba                 import *
from testRole                   import *
from testSprint                 import *
#from testsubEquipoClass         import *
from testTask                   import *
from testTeam                   import *
from testUser                   import *
from testUserHistory            import *

if __name__ == '__main__':
    unittest.main()

