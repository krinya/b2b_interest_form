import streamlit as st
import os
import datetime
import pytz
import base64

def validate_inputs():
    if st.session_state['company_name'] == "":
        st.error("Cégnev nem lehet üres. Kérlek add meg a céged nevét.")
        return False
    if st.session_state['contact_name'] == "":
        st.error("Kapcsolattartó neve nem lehet üres. Kérlek add meg a neved.")
        return False
    if st.session_state['phone_number'] == "":
        st.error("Telefonszám nem lehet üres. Kérlek add meg a telefonszámod.")
        return False
    # telefonszam needs to contains only numbers or "+" sign
    if not st.session_state['phone_number'].replace("+", "").isdigit():
        st.error("Telefonszám nem megfelelő, csak számokat és '+'-t tartalmazhat.")
        return False
    if st.session_state['email'] == "":
        st.error("Email cim nem lehet üres. Kérlek add meg az email cimedet.")
        return False
    if st.session_state['email'].find("@") == -1:
        st.error("Email cím nem megfelelő, nem tartalmaz @ (kukac) karaktert.")
        return False
    if st.session_state['email'].find(".") == -1:
        st.error("Email cím nem megfelelő, nem tartalmaz . (pont) karaktert.")
        return False
    if st.session_state['email'].find(" ") != -1:
        st.error("Az email cím nem megfelelő, nem tartalmazhat szóközt.")
        return False
    if st.session_state['total_cars'] == "" or st.session_state['total_cars'] is None:
        st.error("Az 'Összesen mennyi autóval rendelkezel?' mező nem lehet üres")
        return False
    if st.session_state['monthly_cleaning'] == "" or st.session_state['monthly_cleaning'] is None:
        st.error("A 'Hány autót tervezel takaríttatni havonta?' mező nem lehet ures")
        return False
    if st.session_state['location_zip'] == "" or st.session_state['location_zip'] is None:
        st.error("A Mosás helyszínenek iranyítoszama nem lehet üres mező.")
        return False
    if st.session_state['parking_options'] == "" or st.session_state['parking_options'] is None:
        st.error("A 'Milyen parkolási lehetősegekkel rendelkezel?' mező nem lehet üres.")
        return False
    if st.session_state['car_types'] == "" or st.session_state['car_types'] is None:
        st.error("A 'Milyen autokat szeretnel takarittatni?' mező nem lehet üres.")
        return False
    if st.session_state['heard_from'] == "" or st.session_state['heard_from'] is None:
        st.error("A 'Honnan hallottál rolunk?' mező nem lehet üres.")
        return False
    return True