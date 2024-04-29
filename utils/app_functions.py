import streamlit as st
import os
import datetime
import pytz
import base64

def validate_inputs():
    if st.session_state['company_name'] == "":
        st.error("Cegnev nem lehet ures")
        return False
    if st.session_state['contact_name'] == "":
        st.error("Kapcsolattarto neve nem lehet ures")
        return False
    if st.session_state['phone_number'] == "":
        st.error("Telefonszam nem lehet ures")
        return False
    # telefonszam needs to contains only numbers or "+" sign
    if not st.session_state['phone_number'].replace("+", "").isdigit():
        st.error("Telefonszam nem megfelelo, csak szamokat es '+'-t tartalmazhat")
        return False
    if st.session_state['email'] == "":
        st.error("Email cim nem lehet ures")
        return False
    if st.session_state['email'].find("@") == -1:
        st.error("Email cim nem megfelelo, nem tartalmaz @ karaktert")
        return False
    if st.session_state['email'].find(".") == -1:
        st.error("Email cim nem megfelelo, nem tartalmaz . karaktert")
        return False
    if st.session_state['total_cars'] == "" or st.session_state['total_cars'] is None:
        st.error("Osszesen mennyi autoval rendelkezel? nem lehet ures")
        return False
    if st.session_state['monthly_cleaning'] == "" or st.session_state['monthly_cleaning'] is None:
        st.error("Hany autot tervezel takarittatni havonta? nem lehet ures")
        return False
    if st.session_state['location_zip'] == "" or st.session_state['location_zip'] is None:
        st.error("Mosas helyszinenek iranyitoszama? nem lehet ures")
        return False
    if st.session_state['parking_options'] == "" or st.session_state['parking_options'] is None:
        st.error("Milyen parkolasi lehetosegekkel rendelkezel? nem lehet ures")
        return False
    if st.session_state['car_types'] == "" or st.session_state['car_types'] is None:
        st.error("Milyen autokat szeretnel takarittatni? nem lehet ures")
        return False
    if st.session_state['heard_from'] == "" or st.session_state['heard_from'] is None:
        st.error("Honnan hallottal rolunk? nem lehet ures")
        return False
    return True