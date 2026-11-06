import streamlit as st

st.markdown("""
<style>
.stApp { background-color: #111111; }
.titre { background-color: #FFD400; padding: 20px; border-radius: 15px; text-align: center; }
.titre h1 { color: black; font-size: 32px; margin: 0; }
.titre p { color: black; font-size: 18px; margin: 0; }
div.stButton > button { background-color: black !important; color: #FFD400 !important; border: 2px solid #FFD400 !important; border-radius: 30px !important; padding: 15px !important; font-size: 20px !important; font-weight: bold !important; width: 100%; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="titre"><h1>MBOA TAXI</h1><p>Combien je paie a Yaounde ?</p></div>', unsafe_allow_html=True)
st.write("")

prix = {
    "mokolo-odza": 500,
    "mokolo-centre": 350,
    "odza-centre": 500,
    "mokolo-mvog-mbi": 350,
    "centre-nlongkak": 400,
    "mokolo-biyem-assi": 500,
    "centre-biyem-assi": 500,
    "odza-mvog-mbi": 500,
    "odza-biyem-assi": 900,
    "centre-mendong": 500,
    "mokolo-mendong": 500,
    "centre-etoudi": 500,
    "mokolo-etoudi": 500,
    "odza-etoudi": 700,
    "nlongkak-etoudi": 350,
    "centre-nkolbisson": 500,
    "mokolo-nkolbisson": 500,
    "mvog-mbi-biyem-assi": 500,
    "mvog-mbi-mendong": 400,
    "centre-essos": 500,
    "mokolo-essos": 500,
    "odza-essos": 500,
}

quartiers = ["mokolo", "odza", "centre", "mvog-mbi", "nlongkak", "biyem-assi", "mendong", "etoudi", "nkolbisson", "essos"]

depart = st.selectbox("TU ES OU ?", quartiers)
arrivee = st.selectbox("TU VAS OU ?", quartiers)

if st.button("VOIR LE PRIX"):
    if depart == arrivee:
        st.warning("Tu es deja la !")
    else:
        trajet = depart + "-" + arrivee
        inverse = arrivee + "-" + depart
        if trajet in prix:
            st.success(f"Prix normal : {prix[trajet]} FCFA. Ne paie pas plus !")
        elif inverse in prix:
            st.success(f"Prix normal : {prix[inverse]} FCFA. Ne paie pas plus !")
        else:
            st.warning("On ne connait pas encore ce trajet. Demande au chauffeur avant de monter.")

st.write("")
st.write("---")
st.write("Fait avec amour par cesar. Si un taxi te demande plus, montre-lui l'ecran.")
