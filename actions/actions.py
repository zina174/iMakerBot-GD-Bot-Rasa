# This is a simple example for a custom action which utters "Hello World!"
from typing import Text, List, Dict, Any, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType ,UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from translation import TranslationServiceClient
from rasa_sdk.types import DomainDict
import webbrowser
import locale




loc = locale.getlocale() # get current locale
locale.getdefaultlocale()
default_locale = locale.getdefaultlocale()[0]
lang = default_locale.split("_")
lang_code = lang[0]

class newletterSubscription(Action):
    def name(self) -> Text:
        return "action_newslettersubscription"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_newsletter_subscription')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            dispatcher.utter_message(template='utter_newsletter_subscription_french')
            dispatcher.utter_message(template='utter_replay_main_french')  
        elif (where == 'ar'):
            dispatcher.utter_message(template='utter_newsletter_subscription_arabic')
            dispatcher.utter_message(template='utter_replay_main_arabic')  
        else:
            dispatcher.utter_message('please try to reformulate your question')
            dispatcher.utter_message(template='utter_replay_main')  
        return []

class newletterSubscription_to_page(Action):
    def name(self) -> Text:
        return "action_newslettersubscription_to_page"

    async def run(
    self,
    dispatcher,
    tracker: Tracker,
    domain: "DomainDict",
    ) -> List[Dict[Text, Any]]: 
        newslettersubscription_url="https://www.gdcollect-data.fr/"
        webbrowser.open(newslettersubscription_url)
        return []

class detectLgToCreateAccount(Action):
    def name(self) -> Text:
        return "action_create_account_by_utter"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_create_acount')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            dispatcher.utter_message(template='utter_create_acount_fr')
            dispatcher.utter_message(template='utter_replay_main_french') 
        elif (where == 'ar'):
            dispatcher.utter_message(template='utter_create_acount_ar')
            dispatcher.utter_message(template='utter_replay_main_arabic') 
        else:
            dispatcher.utter_message('please try to reformulate your question')
            dispatcher.utter_message(template='utter_replay_main') 
        return []

class createAccount(Action):
    def name(self) -> Text:
        return "action_create_account"

    async def run(
    self,
    dispatcher,
    tracker: Tracker,
    domain: "DomainDict",
    ) -> List[Dict[Text, Any]]: 
        create_accounr_url="https://www.gdcollect-data.fr/online-training/"
        webbrowser.open(create_accounr_url)
        return []

class Translation(Action):
    
    def name(self) -> Text:
        return "action_respond_to_general_Agent_Capabilities"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_general_Agent_Capabilities')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Hi, I am your customer service chatbot. You can ask me about your account, about courses, payment, anything you want to find about contacting us, and I’ll answer you. You can ask me about any subject related to our startup')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
            dispatcher.utter_message(template='utter_replay_main_french') 
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Hi, I am your customer service chatbot. You can ask me about your account, about courses, payment, anything you want to find about contacting us, and I’ll answer you. You can ask me about any subject related to our startup')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
            dispatcher.utter_message(template='utter_replay_main_arabic') 
        else:
            dispatcher.utter_message('please try to reformulate your question')
            dispatcher.utter_message(template='utter_replay_main') 
        return []

class TranslationSession_commencement(Action):
    
    def name(self) -> Text:
        return "action_respond_to_Session_commencement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_session_commencement')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Exact date has not been decided yet, but we will send you the whole information about session commencement. Please look at our website to be updated')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
            dispatcher.utter_message(template='utter_replay_main_french') 
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Exact date has not been decided yet, but we will send you the whole information about session commencement. Please look at our website to be updated')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
            dispatcher.utter_message(template='utter_replay_main_arabic') 
        else:
            dispatcher.utter_message('please try to reformulate your question')
            dispatcher.utter_message(template='utter_replay_main')            
        return []

class Translationregistration_problems(Action):
    
    def name(self) -> Text:
        return "action_respond_to_registration_problems"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_registration_problems')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('We are sorry about this issue, please contact us on this number (+216)92009902/(+33)354865357 or send an email to contact@gdcollect-data.fr to resolve your problem')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
            dispatcher.utter_message(template='utter_replay_main_french') 
        elif (where == 'ar'):
            dispatcher.utter_message('نحن آسفون بشأن هذه المسألة، يرجى الاتصال بنا على هذا الرقم (+216)92009902/(+33)354865357  أو إرسال بريد إلكتروني للاتصال contact@gdcollect-data.fr لحل مشكلتك')
            dispatcher.utter_message(template='utter_replay_main_arabic') 
        else:
            dispatcher.utter_message('please try to reformulate your question')
            dispatcher.utter_message(template='utter_replay_main') 
        return []

class Translationswitch_account(Action):
    
    def name(self) -> Text:
        return "action_respond_to_switch_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_switch_account')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('To switch your profile you have to log out of your current account and sign in to your desired account, be aware that you have to continue your courses with the registration account')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('To switch your profile you have to log out of your current account and sign in to your desired account, be aware that you have to continue your courses with the registration account')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translationcontact_customer_service(Action):
    
    def name(self) -> Text:
        return "action_respond_to_contact_customer_service"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_contact_customer_service')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('You can contact customer service via phone:\n (+216)92009902/(+33)354865357  or via email:\n contact@gdcollect-data.fr')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            dispatcher.utter_message('نحن آسفون بشأن هذه المسألة، يرجى الاتصال بنا على هذا الرقم (+216)92009902/(+33)354865357  أو إرسال بريد إلكتروني للاتصالcontact@gdcollect-data.fr لحل مشكلتك')
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translationcontact_human_agent(Action):
    
    def name(self) -> Text:
        return "action_respond_to_contact_human_agent"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_contact_human_agent')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('It is possible to contact a human agent via phone:\n (+216)92009902/(+33)354865357\n or via email:\n contact@gdcollect-data.fr')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            dispatcher.utter_message('contact@gdcollect-data.frمن الممكن الاتصال بعامل بشري عن طريق الهاتف:(+216)92009902/(+33)354865357  أو عن طريق البريد الإلكتروني:')
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translationcourse_period(Action):
    
    def name(self) -> Text:
        return "action_respond_to_course_period"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_course_period')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('The course period has not been decided yet, but we will stay in touch with you via email as soon as we set the date. Please look at our website to be updated')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('The course period has not been decided yet, but we will stay in touch with you via email as soon as we set the date. Please look at our website to be updated')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class TranslationCheck_invoices(Action):
    
    def name(self) -> Text:
        return "action_respond_to_check_invoices"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_check_invoices')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Check your email to find all your bills, we send them by email')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Check your email to find all your bills, we send them by email')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_get_invoice(Action):
    
    def name(self) -> Text:
        return "action_respond_to_get_invoice"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_get_invoice')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('All bills are sent by email, check your email box or your spam')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('All bills are sent by email, check your email box or your spam')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_general_Security_Assurance(Action):
    
    def name(self) -> Text:
        return "action_respond_to_general_Security_Assurance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_general_Security_Assurance')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('We took all necessary precautions against fraud and attacks')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('We took all necessary precautions against fraud and attacks')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_general_Negative_Feedback(Action):
    
    def name(self) -> Text:
        return "action_respond_to_general_Negative_Feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_general_Negative_Feedback')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('I\'m sorry about this impression, I\'ll try to imrpove myself, don\'t forget to leave your feedback by the end of this conversation')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('I\'m sorry about this impression, I\'ll try to imrpove myself, don\'t forget to leave your feedback by the end of this conversation')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_general_Positive_Feedback(Action):
    
    def name(self) -> Text:
        return "action_respond_to_general_Positive_Feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_general_Positive_Feedback')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Thanks for your compliments, happy that I helped you')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Thanks for your compliments, happy that I helped you')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_general_Positive_Feedback(Action):
    
    def name(self) -> Text:
        return "action_respond_to_general_Positive_Feedback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_general_Positive_Feedback')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Thanks for your compliments, happy that I helped you')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Thanks for your compliments, happy that I helped you')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_general_Human_or_Bot(Action):
    
    def name(self) -> Text:
        return "action_respond_to_general_Human_or_Bot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_general_Human_or_Bot')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('I\'m a bot developped by Rasa')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('I\'m a bot developped by Rasa')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_delete_account(Action):
    
    def name(self) -> Text:
        return "action_respond_to_delete_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_delete_account')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('You can delete your account any time you want, you log in to your existing account and choose the option delete account')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('You can delete your account any time you want, you log in to your existing account and choose the option delete account')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_edit_account(Action):
    
    def name(self) -> Text:
        return "action_respond_to_edit_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_edit_account')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('You can update your personal informations any time you want, you log in to your existing account and choose the option update account')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('You can update your personal informations any time you want, you log in to your existing account and choose the option update account')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_recover_password(Action):
    
    def name(self) -> Text:
        return "action_respond_to_recover_password"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_recover_password')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('If you forgot your password, click on the option forget password while logging to your account, we will send you an email to type a new password')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('If you forgot your password, click on the option forget password while logging to your account, we will send you an email to type a new password')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_check_cancellation_fee(Action):
    
    def name(self) -> Text:
        return "action_respond_to_check_cancellation_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_check_cancellation_fee')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Once you have enrolled in a course you cannot make a cancellation, that\'s why there isn\'t a cancellation penalty because unbooking isn\'t possible')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Once you have enrolled in a course you cannot make a cancellation, that\'s why there isn\'t a cancellation penalty because unbooking isn\'t possible')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_cancel_course_subscription(Action):
    
    def name(self) -> Text:
        return "action_respond_to_cancel_course_subscription"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_cancel_course_subscription')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('You can\'t cancel your course subscription')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('You can\'t cancel your course subscription')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_change_course(Action):
    
    def name(self) -> Text:
        return "action_respond_to_change_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_change_course')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('We are sorry you can\'t change a course by another one')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('We are sorry you can\'t change a course by another one')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_payment_issue(Action):
    
    def name(self) -> Text:
        return "action_respond_to_payment_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_payment_issue')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Please send an email to contact@gdcollect-data.fr and clarify your payment issue we will check it and contact you as soon as possible')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            dispatcher.utter_message('الرجاء إرسال بريد إلكتروني إلى الاتصالcontact@gdcollect-data.fr وتوضيح مسألة الدفع الخاصة بك سوف نتحقق منه ونتصل بك في أقرب وقت ممكن.')
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_get_refund(Action):
    
    def name(self) -> Text:
        return "action_respond_to_get_refund"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_get_refund')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('If a course is cancelled, all participants will get their money back, in other cases we don\'t pay a refund')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('If a course is cancelled, all participants will get their money back, in other cases we don\'t pay a refund')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_general_About_You(Action):
    
    def name(self) -> Text:
        return "action_respond_to_general_About_You"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_general_About_You')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('I\'m iMaker Bot , a virtual assistant developed by Rasa, I can talk 3 languages(Arabic, French, English) and I\'m here to answer your questions about GD-COLLECT-DATA startup')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('I\'m iMaker Bot, a virtual assistant developed by Rasa, I can talk 3 languages(Arabic, French, English) and I\'m here to answer your questions about GD-COLLECT-DATA startup')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_skills_needed_for_employee(Action):
    
    def name(self) -> Text:
        return "action_respond_to_skills_needed_for_employee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_skills_needed_for_employee')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('For a beginner role a degree usually adds some level of credibility, but if you have a good portfolio with good projects, it is usually an accepted substitute. We hope to see if you are comfortable with basic concepts in programming along with being able to write code. We are looking for developers with good skills in coding, should have good problem solving and analysis skills, should be good with stats and building testing and deploying models.')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('For a beginner role a degree usually adds some level of credibility, but if you have a good portfolio with good projects, it is usually an accepted substitute. We hope to see if you are comfortable with basic concepts in programming along with being able to write code. We are looking for developers with good skills in coding, should have good problem solving and analysis skills, should be good with stats and building testing and deploying models.')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_prepare_for_interview(Action):
    
    def name(self) -> Text:
        return "action_respond_to_prepare_for_interview"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_prepare_for_interview')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Usually the interview has a subset of these rounds==>Resume deep dive, algorithms and technical Concepts, Problem solving test, Coding, Behavioural, Sometimes, some of these rounds might be combined, for instance there might not be two separate rounds for coding and algorithms. Similarly there might be a single round for technical concepts and scenario based problem solving.')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Usually the interview has a subset of these rounds==>Resume deep dive, algorithms and technical Concepts, Problem solving test, Coding, Behavioural, Sometimes, some of these rounds might be combined, for instance there might not be two separate rounds for coding and algorithms. Similarly there might be a single round for technical concepts and scenario based problem solving.')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_out_of_scope(Action):
    
    def name(self) -> Text:
        return "action_respond_to_out_of_scope"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_out_of_scope')
            dispatcher.utter_message(template='utter_replay_main') 
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Sorry, I can\'t handle that request.')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Sorry, I can\'t handle that request.')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class Translation_fallback(Action):
    
    def name(self) -> Text:
        return "action_respond_to_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        #query = tracker.latest_message.get('text')
        #print(query)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template='utter_please_rephrase')
            dispatcher.utter_message(template='utter_replay_main')
        elif (where == 'fr'):
            msg = testInstance.Translate_output('I\'m sorry, I didn\'t quite understand that. Could you rephrase?')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('I\'m sorry, I didn\'t quite understand that. Could you rephrase?')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
            
        return []

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_customized_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template="utter_default")
            dispatcher.utter_message(template='utter_replay_main')
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Sorry I didn\'t get that. Can you rephrase?')
        #msg = Translate_output('B stands for Bidirectional Encoder Representations from Transformers')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Sorry I didn\'t get that. Can you rephrase?')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]

class FormGetSupportPositiveFeedback(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_support_positive_feedback"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["support_positive_feedback"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "support_positive_feedback": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
            
        return []

class FormGetSupportComplaintFeedback(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_support_complaint_feedback"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["support_complaint_feedback"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "support_complaint_feedback": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
            
        return []

class FormGetSupportReviewFeedback(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_support_review_feedback"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["support_review_feedback"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "support_review_feedback": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
            
        return []

class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_ranking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        testInstance = TranslationServiceClient()
        text = tracker.latest_message['text']
        where = next(tracker.get_latest_entity_values('language'), None)
        if (where == 'en'):
            dispatcher.utter_message(text=f"Receiving your Feedback : {text} ")
            dispatcher.utter_message(template="utter_finish")
        elif (where == 'fr'):
            text = testInstance.Translate_output(text)
            dispatcher.utter_message(text=f"Recevoir vos commentaires : {text} ")
            msg = testInstance.Translate_output('I\’m sharing the information on your behalf with our team! You can keep exploring our services and ask me whatever you want to know about our startup')
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            text = testInstance.Translate_output_to_arabic(text)
            dispatcher.utter_message(text=f"تحصلنا على تعليقك: {text} ")
            msg = testInstance.Translate_output_to_arabic('I\’m sharing the information on your behalf with our team! You can keep exploring our services and ask me whatever you want to know about our startup')
            dispatcher.utter_message(str(msg))
        return [SlotSet("complaint", text)]

class ActionHelloWorld(Action):
    def name(self) -> Text:
        """This is the name to be mentioned in domain.yml and stories.md files for this action."""
        return "action_session_start"

    async def run(
      self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[EventType]:

        # the session should begin with a `session_started` event
        events = [SessionStarted()]
        if lang_code =='en':
            dispatcher.utter_message(template="utter_welcome_message")
            dispatcher.utter_message(template="utter_language")
        elif lang_code =='ar':
            dispatcher.utter_message(template="utter_welcome_arabic_message")
            dispatcher.utter_message(template="utter_language_arabic")
        else:
            dispatcher.utter_message(template="utter_welcome_french_message")
            dispatcher.utter_message(template="utter_language_french")

        # an `action_listen` should be added at the end as a user message follows
        events.append(ActionExecuted("action_listen"))
        #return events
        return [events, UserUtteranceReverted()]

class ActionTranslateMdgForRating(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_translate_msg_for_rating"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template="utter_ask_for_rating")
        elif (where == 'fr'):
            msg = testInstance.Translate_output('Because we aim always to improve our services we give you the opportunity to express your opinion, please assess your experience with us?')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('Because we aim always to improve our services we give you the opportunity to express your opinion, please assess your experience with us?')
            print('msg:', msg)
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
        return []
    
class ActionTranslateExpressOpinion(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_translate_express_opinion"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        testInstance = TranslationServiceClient()
        #langs = ids_langid[0]
        #current_intent = tracker.latest_message['intent'].get('name')
        #print('current intent is:', current_intent)
        if (where == 'en'):
            dispatcher.utter_message(template="utter_express_opinion")
        elif (where == 'fr'):
            msg = testInstance.Translate_output('please provide more details here')
            dispatcher.utter_message(str(msg))
        elif (where == 'ar'):
            msg = testInstance.Translate_output_to_arabic('please provide more details here')
            dispatcher.utter_message(str(msg))
        else:
            dispatcher.utter_message('please try to reformulate your question')
        return []

#""""""""""""""""""""""""""""""""#
class FormGetRating(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_rating"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["rating"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "rating": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
            
        return []

class FormGetInfluence(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_influence"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        # decide if the rating is low and ask for influence
        rating = int(tracker.get_slot("rating"))

        if rating < 3:
            return ["influence"]
        else:
            return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "influence": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # decide if the rating is low and send according finish message
        rating = int(tracker.get_slot("rating"))

        if rating < 3:
            dispatcher.utter_template("utter_influence_done", tracker)
        else:
            dispatcher.utter_template("utter_awesome", tracker)
            
        return []

class FormGetSupportFeedback(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_support_feedback"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["support_feedback"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "support_feedback": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
            
        return []

class FormGetRatingQuick(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_get_rating_quick"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["rating_quick"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            "rating_quick": [
                self.from_text(),
            ],
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""
            
        return []

class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_ranking"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Receiving your Feedback : {text} ")
        return [SlotSet("complaint", text)]        



class Translation_multilingual_question(Action):
    
    def name(self) -> Text:
        return "action_respond_to_multilingual_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        where = next(tracker.get_latest_entity_values('language'), None)
        print('the language of the original message is:', where)
        intent =  tracker.latest_message['intent'].get('name')
        print('the intent name is:', intent)
        
        if (where == 'en' and intent== 'SERVICES'):
               dispatcher.utter_message(template='utter_ourservices')
            #    dispatcher.utter_message(template='utter_replay_ourservices')    
        elif (where == 'fr' and intent== 'SERVICES'):  
                dispatcher.utter_message(template='utter_ourservices_French') 
                # dispatcher.utter_message(template='utter_replay_main_french')   
        elif (where == 'ar' and intent== 'SERVICES'):  
                dispatcher.utter_message(template='utter_ourservices_Arabic')
                # dispatcher.utter_message(template='utter_replay_main_arabic')                   

        elif (where == 'en' and intent== 'DEVELOPMENT'):
               dispatcher.utter_message(template='utter_development')
               dispatcher.utter_message(template='utter_replay_main')                
        elif (where == 'fr' and intent== 'DEVELOPMENT'):  
                dispatcher.utter_message(template='utter_development_French') 
                dispatcher.utter_message(template='utter_replay_main_french')                  
        elif (where == 'ar' and intent== 'DEVELOPMENT'):  
                dispatcher.utter_message(template='utter_development_Arabic')
                dispatcher.utter_message(template='utter_replay_main_arabic')    

        elif (where == 'en' and intent== 'CHATBOTS'):
               dispatcher.utter_message(template='utter_chatbots')
               dispatcher.utter_message(template='utter_replay_main')                   
        elif (where == 'fr' and intent== 'CHATBOTS'):  
                dispatcher.utter_message(template='utter_chatbots_French') 
                dispatcher.utter_message(template='utter_replay_main_french')                  
        elif (where == 'ar' and intent== 'CHATBOTS'):  
                dispatcher.utter_message(template='utter_chatbots_Arabic')
                dispatcher.utter_message(template='utter_replay_main_arabic')                    


        elif (where == 'en' and intent== 'TRAINING'):
                dispatcher.utter_message(template='utter_training')
                dispatcher.utter_message(template='utter_replay_main')                  
        elif (where == 'fr' and intent== 'TRAINING'):  
                dispatcher.utter_message(template='utter_training_French') 
                dispatcher.utter_message(template='utter_replay_main_french')                   
        elif (where == 'ar' and intent== 'TRAINING'):  
                dispatcher.utter_message(template='utter_training_Arabic')
                dispatcher.utter_message(template='utter_replay_main_arabic')    

        elif (where == 'en' and intent== 'Networks'):
                dispatcher.utter_message(template='utter_networks')
                dispatcher.utter_message(template='utter_replay_main')                     
        elif (where == 'fr' and intent== 'Networks'):  
                dispatcher.utter_message(template='utter_networks_French') 
                dispatcher.utter_message(template='utter_replay_main_french')                     
        elif (where == 'ar' and intent== 'Networks'):  
                dispatcher.utter_message(template='utter_networks_Arabic') 
                dispatcher.utter_message(template='utter_replay_main_arabic')                    

        elif (where == 'en' and intent== 'REFERENCES'):
                dispatcher.utter_message(template='utter_references')
                dispatcher.utter_message(template='utter_replay_main')     
        elif (where == 'fr' and intent== 'REFERENCES'):  
                dispatcher.utter_message(template='utter_references_French') 
                dispatcher.utter_message(template='utter_replay_main_french')                    
        elif (where == 'ar' and intent== 'REFERENCES'):  
                dispatcher.utter_message(template='utter_references_Arabic') 
                dispatcher.utter_message(template='utter_replay_main_arabic')

        elif (where == 'en' and intent== 'CONTACT'):
                dispatcher.utter_message(template='utter_contact')
                dispatcher.utter_message(template='utter_replay_main')                   
        elif (where == 'fr' and intent== 'CONTACT'):  
                dispatcher.utter_message(template='utter_contact_French') 
                dispatcher.utter_message(template='utter_replay_main_french')                     
        elif (where == 'ar' and intent== 'CONTACT'):  
                dispatcher.utter_message(template='utter_contact_Arabic') 
                dispatcher.utter_message(template='utter_replay_main_arabic')                    


        elif (where == 'en' and intent== 'BLOG'):
               dispatcher.utter_message(template='utter_blog')
               dispatcher.utter_message(template='utter_replay_main')      
        elif (where == 'fr' and intent== 'BLOG'):  
                dispatcher.utter_message(template='utter_blog_French') 
                dispatcher.utter_message(template='utter_replay_main_french')                    
        elif (where == 'ar' and intent== 'BLOG'):  
                dispatcher.utter_message(template='utter_blog_Arabic')     
                dispatcher.utter_message(template='utter_replay_main_arabic')              
        else:
            if where == 'en' :
               dispatcher.utter_message("I don't understand your question. Would you please reformulate your question in a different way, please?")                 
            elif where == 'ar' :
               dispatcher.utter_message('أنا لا أفهم سؤالك. هل تسمح بإعادة صياغة سؤالك بطريقة مختلفة من فضلك؟') 
            elif where == 'fr' :
               dispatcher.utter_message("Je ne comprends pas ta question. Pourriez-vous s'il vous plaît reformuler votre question d'une manière différente, s'il vous plaît?")    
        return []