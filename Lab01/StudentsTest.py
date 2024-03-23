import unittest
import Students

class Test(unittest.TestCase):
    students = Students.Students()

    user_name = ['John', 'Mary','Thomas','Jane']
    user_id = []

    # test case function to check the Students.set_name function
    def test_0_set_name(self):
        print("Start set_name test")
        for i, name in enumerate(self.user_name):
            id = self.students.set_name(name)
            self.assertTrue(id >= 0)
            self.assertEqual(id, i)
            self.assertNotIn(id, self.user_id)

            self.user_id.append(id)
            print(f"{id} {name}")
        
        print("Finish set_name test")
        #TODO
        pass
    
    def get_mex(self, arr):
        # constrain: 1. no duplicate 2. elements in the list is non-negative integer
        lst = sorted(arr)
        mex = 0
        for i in lst:
            if i == mex:
                mex += 1
            else:
                break
        return mex

    # test case function to check the Students.get_name function
    def test_1_get_name(self):
        print(f"user_id length =  {len(self.user_id)}")
        print(f"user_name length =  {len(self.user_name)}")
        self.assertEqual(len(self.user_id), len(self.user_name))

        for i, id in enumerate(self.user_id):
            name = self.students.get_name(id)
            self.assertEqual(name, self.user_name[i])
            print(f"id {id} : {name}")
        
        # additional test
        # find the mex id in the list
        id = min(self.user_id)

        name = self.students.get_name(self.get_mex(self.user_id))
        self.assertEqual(name, 'There is no such user')

        print("Finish get_name test")
        #TODO
        pass