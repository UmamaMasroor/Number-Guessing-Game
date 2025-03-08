import streamlit as st
import random

def init_game():
    st.session_state['number'] = random.randint(st.session_state['low'], st.session_state['high'])
    st.session_state['attempts'] = 0
    st.session_state['max_attempts'] = st.session_state['difficulty']
    st.session_state['game_over'] = False
    st.session_state['message'] = "Start guessing!"

def main():
    st.title("Number Guessing Game")
    
    if 'low' not in st.session_state:
        st.session_state['low'] = 1
    if 'high' not in st.session_state:
        st.session_state['high'] = 100
    if 'difficulty' not in st.session_state:
        st.session_state['difficulty'] = 10
    if 'number' not in st.session_state:
        init_game()
    
    with st.sidebar:
        st.header("Game Settings")
        st.session_state['low'] = st.number_input("Lower Bound", min_value=1, max_value=1000, value=1)
        st.session_state['high'] = st.number_input("Upper Bound", min_value=10, max_value=1000, value=100)
        difficulty = st.selectbox("Difficulty Level", ["Easy", "Medium", "Hard"], index=1)
        st.session_state['difficulty'] = {"Easy": 15, "Medium": 10, "Hard": 5}[difficulty]
        if st.button("Restart Game"):
            init_game()
    
    guess = st.number_input("Enter your guess:", min_value=st.session_state['low'], max_value=st.session_state['high'], step=1)
    
    if st.button("Submit Guess") and not st.session_state['game_over']:
        st.session_state['attempts'] += 1
        if guess < st.session_state['number']:
            st.session_state['message'] = "Too low! Try again."
        elif guess > st.session_state['number']:
            st.session_state['message'] = "Too high! Try again."
        else:
            st.session_state['message'] = f"Congratulations! You guessed it in {st.session_state['attempts']} attempts."
            st.session_state['game_over'] = True
        
        if st.session_state['attempts'] >= st.session_state['max_attempts'] and not st.session_state['game_over']:
            st.session_state['message'] = f"Game over! The number was {st.session_state['number']}. Try again!"
            st.session_state['game_over'] = True
    
    st.write(st.session_state['message'])
    st.write(f"Attempts: {st.session_state['attempts']}/{st.session_state['max_attempts']}")

if __name__ == "__main__":
    main()
