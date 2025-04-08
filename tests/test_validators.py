from unittest import TestCase
import validators


class TestValidators(TestCase):
    
    

    def test_name_validator_returns_true_if_name_is_valid(self):
        name = "John Doe"
        result = validators.name_is_valid(name)

        self.assertTrue(result)


    def test_name_validator_returns_false_if_name_has_less_than_3_chars(self):

        name = "Jd"
        result = validators.name_is_valid(name)

        self.assertFalse(result)

    def test_name_validator_returns_false_if_name_has_digit_or_especial_chars(self):

        name1= "John Doe1"
        name2 = "John_Doe"

        result1 = validators.name_is_valid(name1)
        result2 = validators.name_is_valid(name2)

        self.assertFalse(result1)
        self.assertFalse(result2)


    def test_email_validator_returns_true_if_email_is_valid(self):

        email = "email@mail.com"
        result = validators.email_is_valid(email)

        self.assertTrue(result)


    def test_email_validator_returns_false_if_email_dont_have_at_or_dot(self):
        
        email1 = "email$mail.com"
        email2 = "email@mail_com"

        result1 = validators.email_is_valid(email1)
        result2 = validators.email_is_valid(email2)

        self.assertFalse(result1)
        self.assertFalse(result2)

    def test_email_validator_returns_false_if_email_at_is_different_than_one(self):
        
        email1 = "em@ail@mail.com"
        email2 = "email_mail_com"

        result1 = validators.email_is_valid(email1)
        result2 = validators.email_is_valid(email2)

        self.assertFalse(result1)
        self.assertFalse(result2)

    def test_email_validator_returns_false_if_email_starts_or_ends_with_at(self):
        
        email1 = "@email_mail.com"
        email2 = "email_mail.com@"

        result1 = validators.email_is_valid(email1)
        result2 = validators.email_is_valid(email2)

        self.assertFalse(result1)
        self.assertFalse(result2)

    def test_date_validator_returns_true_if_date_is_valid(self):
        
        date = "2099-04-07"
        result = validators.date_is_valid(date)

        self.assertTrue(result)

    def test_date_validator_returns_false_if_date_is_in_the_past(self):

        date = "2000-04-07"
        result = validators.date_is_valid(date)

        self.assertFalse(result)

    def test_date_validator_returns_false_if_date_has_invalid_format(self):

        date = "2000/04/07"
        result = validators.date_is_valid(date)

        self.assertFalse(result)

    def test_index_validator_returns_true_if_index_is_valid(self):

        menu = [
            { 0 : "2025-04-07T14:30:00.000Z"},
            { 1 : "2025-04-07T14:45:00.000Z"},
            ]
        
        index = "1"

        result = validators.index_is_valid(index, menu)

        self.assertTrue(result)

    def test_index_validator_returns_false_if_index_out_of_the_range(self):

        menu = [
            { 0 : "2025-04-07T14:30:00.000Z"},
            { 1 : "2025-04-07T14:45:00.000Z"},
            ]
        
        index = "3"

        result = validators.index_is_valid(index, menu)

        self.assertFalse(result)

    def test_index_validator_returns_false_if_negative_index_or_isnt_a_digit(self):

        menu = [
            { 0 : "2025-04-07T14:30:00.000Z"},
            { 1 : "2025-04-07T14:45:00.000Z"},
            ]
        
        index1 = "a"
        index2 = "-1"


        result1 = validators.index_is_valid(index1, menu)
        result2 = validators.index_is_valid(index2, menu)

        self.assertFalse(result1)
        self.assertFalse(result2)

