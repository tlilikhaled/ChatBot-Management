
from typing import Any, Text, Dict, List
from rasa_sdk.types import DomainDict
from rasa_sdk import Action, Tracker, FormValidationAction
from dateutil import parser
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
    UserUtteranceReverted,
)


from actions.custom_forms import CustomFormValidationAction
from database.connection_db import (
    salary_dev, 
    salary_qa,
    salary_devops,
    salary_support,
    last_date_dev, 
    last_date_qa,
    last_date_devops,
    last_date_sup,
    list_known_projects_Id, 
    sum_salary_project
)

   
class ActionKnowSumSalary(Action):
    """ Know Sum Salary"."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_sum_salary"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict]:
        """Executes the action"""
        slots = {
            "project_id": None,
        }
        print(tracker.get_slot("project_id") )
        Id = tracker.get_slot("project_id")
        print(Id) 
        Id1 = str(Id)   
        known_Id = list_known_projects_Id()
        if Id is not None and Id1  in known_Id:
            res = sum_salary_project(Id)
            dispatcher.utter_message(text=f" The Sum Salaries of your project is $ {res} ") 
            dispatcher.utter_message(response="utter_ask_whatelse") 
        else:
            dispatcher.utter_message(response="utter_unknown_project_id")

        return [SlotSet(slot, value) for slot, value in slots.items()]



class ActionKnowSalaryOfGrade(Action):
    """Know Salary Of Grade"."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_grade_salary"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict]:
        """Executes the action"""
        slots = {
            "grade": None,
        }

              
        print(tracker.get_slot("grade"))
        if tracker.get_slot("grade") == "Developer":
            salaire_dev = salary_dev()
            dispatcher.utter_message(text=f" The salary of grade Developer is $ {salaire_dev} ")
            dispatcher.utter_message(response="utter_ask_whatelse") 
        if tracker.get_slot("grade") == "Quality":
            salaire_qa = salary_qa()
            dispatcher.utter_message(text=f" The salary of grade Quality is $ {salaire_qa} ")
            dispatcher.utter_message(response="utter_ask_whatelse") 
        if tracker.get_slot("grade") == "DevOps":
            salaire_devops = salary_devops()
            dispatcher.utter_message(text=f" The salary of grade Devops is $ {salaire_devops} ")
            dispatcher.utter_message(response="utter_ask_whatelse") 
        if tracker.get_slot("grade") == "IT Support":
            salaire_supp = salary_support()
            dispatcher.utter_message(text=f" The salary of grade Support is $ {salaire_supp} ")
            dispatcher.utter_message(response="utter_ask_whatelse") 
      


        return [SlotSet(slot, value) for slot, value in slots.items()]

    
class ValidateKnowGradeForm(CustomFormValidationAction):
    """Validates Slots of the know_grade_form"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "validate_know_grade_form"
    
    async def validate_grade(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validates value of 'grade' slot"""
        print("validation start")
        print(value)
        List = ["Developer", "Quality","DevOps","IT Support"]
        print(value in List)
        if value in List:
            return {"grade": value}
        
        dispatcher.utter_message(response="utter_unknown_grade")
        return {"grade": None}


class ActionShowInfoGrade(Action):
    """Shows Informmations about grade employee"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_show_info_grade"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict]:
        """Executes the action"""
     
        res = last_date_dev()
        result = salary_dev()
        res1 = last_date_qa()
        result1 = salary_qa()
        res2 = last_date_devops()
        result2 = salary_devops()
        res3 = last_date_sup()
        result3 = salary_support()
        dispatcher.utter_message(text=f"[Grade: Developer, Salary: {result}, Last Date Update : {res}]")
        dispatcher.utter_message(text=f"[Grade: Quality, Salary: {result1}, Last Date Update : {res1}]")
        dispatcher.utter_message(text=f"[Grade: DevOps, Salary: {result2}, Last Date Update : {res2}]")
        dispatcher.utter_message(text=f"[Grade: IT Support, Salary: {result3}, Last Date Update : {res3}]")
        dispatcher.utter_message(response="utter_ask_whatelse") 
        return []
    
class ValidateSumSalaryForm(CustomFormValidationAction):
    """Validates Slots of the sum_salary_form"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "validate_sum_salary_form"

    
    async def validate_people_ressource(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validates value of 'people_ressource' slot"""
        if int(value) <= 0:
            dispatcher.utter_message(text=f" We only accept number of people ressource > 0")
            return {"people_ressource": None}
        return {"people_ressource": value}
    
    
    
    async def validate_developer(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validates value of 'developer' slot"""
        if int(value) < 0:
            dispatcher.utter_message(text=f" We only accept number of profil developer >= 0")
            return {"developer": None}
        return {"developer": value}
    
    async def validate_quality(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validates value of 'quality' slot"""
        if int(value) < 0:
            dispatcher.utter_message(text=f" We only accept number of profil QA >= 0")
            return {"quality": None}
        return {"quality": value}
    async def validate_devops(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validates value of 'devops' slot"""
        if int(value) < 0:
            dispatcher.utter_message(text=f" We only accept number of profil devops >= 0")
            return {"devops": None}
        return {"devops": value}
    

    
    async def validate_support(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validates value of 'support' slot"""
        if int(value) < 0:
            dispatcher.utter_message(text=f" We only accept number of profil IT support >= 0")
            return {"support": None}
        return {"support": value}


    async def validate_delivery_date(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validates value of 'delivery_date' slot"""
    
        currDate = datetime.datetime.now().date()
        if value <= str(currDate):
            dispatcher.utter_message(text=f" The end Job date for resource must be greater than {currDate} ")
            return {"delivery_date": None}
        return {"delivery_date": value}


    async def validate_zz_confirm_form(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validates value of 'zz_confirm_form' slot"""
        if value in ["yes", "no"]:
            return {"zz_confirm_form": value}

        return {"zz_confirm_form": None}
    
class ActionCalculSumSalarie(Action):
    """Know Salary Of Grade"."""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_calculate_salary"

    async def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[Dict]:
        """Executes the action"""
        slots = {
            "zz_confirm_form": None,
            "people_ressource":None,
            "developer":None,
            "quality":None,
            "devops":None,
            "support":None,
            "delivery_date":None
        }

              
        if tracker.get_slot("zz_confirm_form") == "yes":
            people_ressource = int(tracker.get_slot("people_ressource"))
            developer= int(tracker.get_slot("developer"))
            quality= int(tracker.get_slot("quality"))
            devops= int(tracker.get_slot("devops"))
            support= int(tracker.get_slot("support"))
            end_date = tracker.get_slot("delivery_date")
            start_date = datetime.datetime.now()
            end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            nb_dt = end - start_date
            nb_dd = nb_dt.days
            nb_mm = nb_dd // 30
            salaire_dev = salary_dev()
            sum_developers = float(salaire_dev) * float(developer)
            salaire_qa = salary_qa()
            sum_qualitys = float(salaire_qa) * float(quality)
            salaire_devops = salary_devops()
            sum_devops = float(salaire_devops) * float(devops)
            salaire_supp = salary_support()
            sum_support = float(salaire_supp) * float(support)
            sum_totale = (sum_developers + sum_devops + sum_qualitys + sum_support) * float(nb_mm)
            dispatcher.utter_message(text=f" The Sum Salaries for its {people_ressource} peoples you need is $ {sum_totale}")
            dispatcher.utter_message(response="utter_ask_whatelse") 
        else:
            dispatcher.utter_message(response="utter_ask_whatelse")


        return [SlotSet(slot, value) for slot, value in slots.items()]

class ActionSessionStart(Action):
    """Executes at start of session"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_session_start"

    @staticmethod
    def _slot_set_events_from_tracker(
        tracker: "Tracker",
    ) -> List["SlotSet"]:
        """Fetches SlotSet events from tracker and carries over keys and values"""

        # when restarting most slots should be reset
        relevant_slots = ["grade"]

        return [
            SlotSet(
                key=event.get("name"),
                value=event.get("value"),
            )
            for event in tracker.events
            if event.get("event") == "slot" and event.get("name") in relevant_slots
        ]
    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Executes the custom action"""
        # the session should begin with a `session_started` event
        events = [SessionStarted()]

        events.extend(self._slot_set_events_from_tracker(tracker))


        # add `action_listen` at the end
        events.append(ActionExecuted("action_listen"))

        return events
class ActionRestart(Action):
    """Executes after restart of a session"""

    def name(self) -> Text:
        """Unique identifier of the action"""
        return "action_restart"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Executes the custom action"""
        return [Restarted(), FollowupAction("action_session_start")]
