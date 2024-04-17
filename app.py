import streamlit as st

def find_largest(x, y, z):
    return max(x, y, z)

def main():
    st.title("Find the Largest Number")
    st.write("Enter three numbers below to find the largest among them.")

    x = st.number_input("Enter the first number:")
    y = st.number_input("Enter the second number:")
    z = st.number_input("Enter the third number:")

    if st.button("Find Largest"):
        largest = find_largest(x, y, z)
        st.success(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
