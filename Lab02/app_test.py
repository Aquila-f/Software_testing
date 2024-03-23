import unittest
from app import Application, MailSystem
from unittest.mock import patch

class ApplicationTest(unittest.TestCase):

    name_list = ["William", "Oliver", "Henry", "Liam"]
    selected_list = ["William", "Oliver", "Henry"]

    @patch.object(Application, 'get_names')
    def setUp(self, mock_get_names):
        # stub
        mock_get_names.return_value = (self.name_list, self.selected_list)
        self.app = Application()
        self.assertEqual(self.app.people, self.name_list)
        self.assertEqual(self.app.selected, self.selected_list)
        pass


    @patch.object(MailSystem, 'write')
    @patch.object(MailSystem, 'send')
    @patch.object(Application, 'get_random_person')
    def test_app(self, mock_get_random_person, mock_send, mock_write):
        # mock
        # check if the selected person is in the selected list
        mock_get_random_person.side_effect = ["William", "Oliver", "Henry", "Liam"]
        old_selected = self.app.selected.copy()
        next_person = self.app.select_next_person()
        self.assertNotIn(next_person, old_selected)
        self.assertEqual(next_person, "Liam")
        print(f"{next_person} selected")

        # spy
        mock_write.side_effect = lambda name: f'Congrats, {name}!'
        mock_send.side_effect = lambda name, context: print(f'{context}')

        self.app.notify_selected()

        print()
        print()
        print(mock_write.call_args_list)
        print(mock_send.call_args_list)

        self.assertEqual(mock_write.call_count, mock_send.call_count)
        
        pass


# if __name__ == "__main__":
#     unittest.main()