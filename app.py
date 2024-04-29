import streamlit as st
import os
import datetime
import pytz
import base64
from utils.app_functions import validate_inputs

# set the page layout and title
st.set_page_config(layout="centered", page_title="CleanGo B2B Erdeklodesi Felulet", page_icon="img/cleango-logo-small.png")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if 'send_in_button_pressed' not in st.session_state:
    st.session_state['send_in_button_pressed'] = 0

def form_send_in_button_press():
    st.session_state['send_in_button_pressed'] = 1

if 'first_step_button_pressed' not in st.session_state:
    st.session_state['first_step_button_pressed'] = 0

def form_first_step_button_press():
    st.session_state['first_step_button_pressed'] = 1

st.markdown(f'![CleanGo Logo](https://cleango.hu/sitebuild/img/logo-text.svg)')
st.markdown("# B2B Árajánlat kérő felület")
st.markdown(":car: Ha szeretnél B2B árajánlatot kapni a CleanGo-tol, akkor töltsd ki az alabbi ürlapot, és mi pár napon belül felvesszuk veled a kapcsolatot. :car:")

main_cointainer = st.container(border=True)

# Create a form container
with main_cointainer:
    st.markdown("#### Kapcsolati adatok")
    st.text_input("Cégnev", key="company_name")
    st.text_input("Kapcsolattartó neve", key="contact_name", placeholder="Vezetéknév Keresztnév")
    st.text_input("Telefonszám", key="phone_number", placeholder="+36")
    st.text_input("Email cím", key="email")
    st.markdown("#### Mosásra vonatkozó adatok")
    st.number_input("Összesen mennyi autóval rendelkezel?", key="total_cars", min_value=0, value=None)
    st.number_input("Hány autót tervezel takaríttatni havonta?", key="monthly_cleaning", min_value=0, value=None)
    st.number_input("Mosás helyszinének iranyítószáma?", key="location_zip", min_value=1000, max_value = 10000, value=None, placeholder=1234)
    list_of_parking_options = ["Fedett", "Szabadtéri", "Mindkettő"]
    st.radio("Milyen parkolási lehetőségekkel rendelkezel?", list_of_parking_options, key="parking_options", index=None)
    list_of_car_types_options = ["Személyautó", "Nem Személyautó", "Mindkettő"]
    st.radio("Milyen autókat szeretnél takaríttatni?", list_of_car_types_options, key="car_types", index=None)
    st.markdown("#### Egyéb informaciok")
    # dropdown
    list_of_heared_from_us_options = ["Google", "Facebook", "Ismerős ajánlotta", "Egyéb"]
    st.selectbox("Honnan hallottál rólunk?", list_of_heared_from_us_options, key="heard_from", index=None, placeholder="Kerjük válassz a listából.")
    st.text_area("Egyéb bármi más megjegyzés, speciális kérdés", key="comments", placeholder="Ide írhatod a megjegyzéseidet")
    st.button("Árajánlat beküldése", on_click=form_send_in_button_press)

if st.session_state['send_in_button_pressed'] == 1:

    validate_inputs_true_false = validate_inputs()

    if validate_inputs_true_false:

        st.success("Koszonjuk! Az árajánlat kérést sikeresen megkaptuk. Hamarosan felvesszük veled a kapcsolatot.")
        st.markdown("Addig nézd meg a kovetkező dolgokat: és ide irhatunk bármit, amit szeretnénk.")
        
        filled_in_data_container = st.container(border=True)

        with filled_in_data_container:
            st.markdown("#### Az elküldott árajánlat kérés tartalma")
            st.markdown(f"Cégnev: {st.session_state['company_name']}")
            st.markdown(f"Kapcsolattartó neve: {st.session_state['contact_name']}")
            st.markdown(f"Telefonszám: {st.session_state['phone_number']}")
            st.markdown(f"Email cím: {st.session_state['email']}")
            st.markdown(f"Összesen mennyi autóval rendelkezel?: {st.session_state['total_cars']}")
            st.markdown(f"Hány autot tervezel takaríttatni havonta?: {st.session_state['monthly_cleaning']}")
            st.markdown(f"Mosás helyszinének iranyítószáma?: {st.session_state['location_zip']}")
            st.markdown(f"Milyen parkolási lehetőségekkel rendelkezel?: {st.session_state['parking_options']}")
            st.markdown(f"Milyen autókat szeretnél takaríttatni?: {st.session_state['car_types']}")
            st.markdown(f"Honnan hallottál rólunk?: {st.session_state['heard_from']}")
            st.markdown(f"Egyéb bármi más megjegyzés, speciális kérdés: {st.session_state['comments']}")
    else:
        st.error("Az árajánlat kérés nem sikerült, kérjük ellenőrizd az adatokat és próbáld újra. Köszönjük!")

    st.session_state['send_in_button_pressed'] = 0

# st.markdown("---")

# st.markdown("The form structure was last updated on:")
# # get the latest date of the files within the pages folder
# pages_folder = os.path.join(os.getcwd())
# files = os.listdir(pages_folder)
# files.sort(reverse=True)

# #create a max_date variable with a default value
# max_date = datetime.datetime(2021, 1, 1, 0, 0, 0, 0)
# # get the modification time of a file
# for file in files:
#     modification_time = os.path.getmtime(os.path.join(pages_folder, file))
#     # convert timestamp to datetime and local is set to Europe/Amsterdam
#     last_update = datetime.datetime.fromtimestamp(modification_time)
#     # modifiy the max_date if the last_update is greater than the max_date
#     if last_update > max_date:
#         max_date = last_update

# # foromat max_date to show only yyyy-mm-dd
# max_date_yyyy_mm_dd = max_date.strftime("%Y-%m-%d")
# st.markdown(max_date_yyyy_mm_dd)

# st.write("Streamlit version: ", st.__version__)