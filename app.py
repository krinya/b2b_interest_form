import streamlit as st
import os
import datetime
import pytz
import base64

# set the page layout and title
st.set_page_config(layout="centered", page_title="CleanGo B2B Erdeklodesi Felulet")

if 'first_step_button_pressed' not in st.session_state:
    st.session_state['first_step_button_pressed'] = 0

if 'send_in_button_pressed' not in st.session_state:
    st.session_state['send_in_button_pressed'] = 0

def form_send_in_button_press():
    st.session_state['send_in_button_pressed'] = 1

def form_first_step_button_press():
    st.session_state['first_step_button_pressed'] = 1

def validate_inputs():
    if st.session_state['email'] == "":
        st.error("Email cim nem lehet ures")
        return False
    if st.session_state['email'].find("@") == -1:
        st.error("Email cim nem megfelelo, nem tartalmaz @ karaktert")
        return False
    if st.session_state['email'].find(".") == -1:
        st.error("Email cim nem megfelelo, nem tartalmaz . karaktert")
        return False
    if st.session_state['company_name'] == "":
        st.error("Cegnev nem lehet ures")
        return False
    if st.session_state['contact_name'] == "":
        st.error("Kapcsolattarto neve nem lehet ures")
        return False
    if st.session_state['phone_number'] == "":
        st.error("Telefonszam nem lehet ures")
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

st.markdown("# CleanGo B2B Erdeklodesi Felulet")
st.markdown("Ha szeretne ajanlatot kapni, kerjuk toltse ki az alabbi formot.")

main_cointainer = st.container(border=True)

# Create a form container
with main_cointainer:
    st.markdown("#### Kapcsolati adatok")
    st.text_input("**Cegnev**", key="company_name")
    st.text_input("Kapcsolattarto neve", key="contact_name")
    st.text_input("Telefonszam", key="phone_number")
    st.text_input("Email cim", key="email")
    st.markdown("#### Mosasra vonatkozo adatok")
    st.number_input("Osszesen mennyi autoval rendelkezel?", key="total_cars", min_value=0, value=None)
    st.number_input("Hany autot tervezel takarittatni havonta?", key="monthly_cleaning", min_value=0, value=None)
    st.number_input("Mosas helyszinenek iranyitoszama?", key="location_zip", min_value=1000, max_value = 10000, value=None)
    list_of_parking_options = ["Fedett", "Szabadteri", "Mindketto"]
    st.radio("Milyen parkolasi lehetosegekkel rendelkezel?", list_of_parking_options, key="parking_options", index=None)
    list_of_car_types_options = ["Szemelyauto", "Nem szemelyauto", "Mindketto"]
    st.radio("Milyen autokat szeretnel takarittatni?", list_of_car_types_options, key="car_types", index=None)
    st.markdown("#### Egyeb informaciok")
    # dropdown
    list_of_heared_from_us_options = ["Google", "Facebook", "Ismeros", "Egyeb"]
    st.selectbox("Honnan hallottal rolunk?", list_of_heared_from_us_options, key="heard_from", index=None, placeholder="Kerjuk valassz")
    st.text_area("Egyeb barmi mas megjegyzes", key="comments")
    st.button("Kovetkezo lepes", on_click=form_first_step_button_press)

if st.session_state['first_step_button_pressed'] == 1:

    validate_inputs_true_false = validate_inputs()

    filled_in_data_container = st.container(border=True)
    with filled_in_data_container:
        st.write("Ajanlatkeres tartalma:")
        st.write("Cegnev: ", st.session_state['company_name'])
        st.write("Kapcsolattarto neve: ", st.session_state['contact_name'])
        st.write("Telefonszam: ", st.session_state['phone_number'])
        st.write("Email cim: ", st.session_state['email'])
        st.write("Osszesen mennyi autoval rendelkezel?: ", st.session_state['total_cars'])
        st.write("Hany autot tervezel takarittatni havonta?: ", st.session_state['monthly_cleaning'])
        st.write("Mosas helyszinenek iranyitoszama?: ", st.session_state['location_zip'])
        st.write("Milyen parkolasi lehetosegekkel rendelkezel?: ", st.session_state['parking_options'])
        st.write("Milyen autokat szeretnel takarittatni?: ", st.session_state['car_types'])
        st.write("Honnan hallottal rolunk?: ", st.session_state['heard_from'])
        st.write("Egyeb barmi mas megjegyzes: ", st.session_state['comments'])
        st.button("Kuld", on_click=form_send_in_button_press)

    if st.session_state['send_in_button_pressed'] == 1:
        if validate_inputs_true_false:
            st.success("Az ajanlatkeres sikeresen elkuldve.")
        else:
            st.error("Az ajanlatkeres nem sikerult, mert nem toltotte ki helyesen a mezoket.")
        st.session_state['send_in_button_pressed'] = 0

st.markdown("---")

st.markdown("The form structure was last updated on:")
# get the latest date of the files within the pages folder
pages_folder = os.path.join(os.getcwd())
files = os.listdir(pages_folder)
files.sort(reverse=True)

#create a max_date variable with a default value
max_date = datetime.datetime(2021, 1, 1, 0, 0, 0, 0)
# get the modification time of a file
for file in files:
    modification_time = os.path.getmtime(os.path.join(pages_folder, file))
    # convert timestamp to datetime and local is set to Europe/Amsterdam
    last_update = datetime.datetime.fromtimestamp(modification_time)
    # modifiy the max_date if the last_update is greater than the max_date
    if last_update > max_date:
        max_date = last_update

# foromat max_date to show only yyyy-mm-dd
max_date_yyyy_mm_dd = max_date.strftime("%Y-%m-%d")
st.markdown(max_date_yyyy_mm_dd)

st.write("Streamlit version: ", st.__version__)