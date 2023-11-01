
#demo
import streamlit as st
import cohere
import os
api_key = os.environ.get('CO_API_KEY')
co = cohere.Client(api_key)
def generate_haiku(name,hobby):
    """Generate a haiku given the name and hobby provided as inputs
    Arguments: name (str)
    hobby (str)
    Returns:
    HAIKU: a haiku given the name and hobby inputs (str)
    """

    prompt = f"""Generate a haiku using the provided NAME and HOBBY. Here are a few examples.

    NAME: Squidward
    HOBBY: playing the clarinet
    HAIKU: Squidward's heart in tune,
    Clarinet whispers the sea,
    Notes of longing croon.
    --
    NAME: Bruno
    HOBBY: making zippers
    HAIKU:Bruno's nimble hands,
    Zippers dance at his command,
    Seamless art expands.

    --
    NAME: Roy
    HOBBY: flame alchemy
    HAIKU: Flames in Roy's control,
    Alchemy's fierce, burning soul,
    Inferno takes its toll.

    --

    NAME: Joey
    HOBBY: backpacking through Western Europe
    HAIKU:Joey roams the West,
    Backpack and dreams manifest,
    Europe's heart, his quest.

    NAME: {name}
    HOBBY: {hobby}
    HAIKU:
    """
        # Call the Cohere Generate endpoint
    response = co.generate(
        model="command-nightly",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        k=0,
        stop_sequences=["--"],
    )

    HAIKU = response.generations[0].text
    HAIKU = HAIKU.replace("\n\n--", "").replace("\n--", "").strip()
    return HAIKU

def run():
    st.title("NAME👋 HOBBY🫶 HAIKU GENERATOR")
    name = st.text_input("Name:", placeholder="Squidward")
    hobby = st.text_input("Hobby:", placeholder = "Playing the clarinet")

    if st.button("Generate"):
        if name and hobby:
            HAIKU = generate_haiku(name,hobby)
        st.write(HAIKU.replace("\n","\n\n"))

if __name__ == "__main__":
    run()