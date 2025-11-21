# # import tkinter as tk

# # # Window setup
# # root = tk.Tk()
# # root.title("Modern Calculator")
# # root.geometry("400x500")
# # root.config(bg="#2b2b2b")  # Dark background

# # # Entry box (for input/result)
# # entry = tk.Entry(root, font=("Arial", 28), bg="#3b3b3b", fg="white", bd=0, justify="right")
# # entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

# # # Button click function
# # def button_click(number):
# #     current = entry.get()
# #     entry.delete(0, tk.END)
# #     entry.insert(0, current + str(number))

# # # Clear function
# # def button_clear():
# #     entry.delete(0, tk.END)

# # # Equal function
# # def button_equal():
# #     try:
# #         result = eval(entry.get())
# #         entry.delete(0, tk.END)
# #         entry.insert(0, str(result))
# #     except:
# #         entry.delete(0, tk.END)
# #         entry.insert(0, "Error")

# # # Button style
# # button_style = {
# #     "font": ("Arial", 20),
# #     "bg": "#4d4d4d",
# #     "fg": "white",
# #     "bd": 0,
# #     "width": 5,
# #     "height": 2,
# #     "activebackground": "#6b6b6b"
# # }

# # operator_style = button_style.copy()
# # operator_style.update({"bg": "#ff9500", "activebackground": "#ffa733"})

# # # Number buttons
# # buttons = [
# #     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
# #     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
# #     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
# #     ('0', 4, 0)
# # ]

# # for (text, row, col) in buttons:
# #     tk.Button(root, text=text, command=lambda t=text: button_click(t), **button_style)\
# #         .grid(row=row, column=col, padx=5, pady=5)

# # # Operator buttons
# # operators = [
# #     ('+', 1, 3), ('-', 2, 3),
# #     ('*', 3, 3), ('/', 4, 3),
# #     ('C', 4, 1), ('=', 4, 2)
# # ]

# # for (text, row, col) in operators:
# #     if text == 'C':
# #         tk.Button(root, text=text, command=button_clear, **operator_style)\
# #             .grid(row=row, column=col, padx=5, pady=5)
# #     elif text == '=':
# #         tk.Button(root, text=text, command=button_equal, **operator_style)\
# #             .grid(row=row, column=col, padx=5, pady=5)
# #     else:
# #         tk.Button(root, text=text, command=lambda t=text: button_click(t), **operator_style)\
# #             .grid(row=row, column=col, padx=5, pady=5)

# # root.mainloop()




# print("1 - Add")
# print("2 - Subtract")
# print("3 - Divide")
# print("4 - Multiply")
# Option = int(input("choose an operation:"))

# if (Option in [1,2,3,4]):
#     num1 = int(input("enter your 1st number:"))
#     num2 = int(input("enter your 2nd number:"))
#     if (Option == 1):
#         result = num1 + num2 
#     elif(Option == 2):
#         result = num1 * num2
#     elif(Option == 3):
#         result = num1 // num2
#     elif(Option == 4):
#         result = num1 - num2 


# else:
#     print("invalid operation enter ")

# print("The result of the operation is {}".format(result))


# from flask import Flask, render_template, request

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def calculator():
#     result = None
    
#     if request.method == "POST":
#         option = request.form.get("operation")
#         num1 = float(request.form.get("num1"))
#         num2 = float(request.form.get("num2"))

#         if option == "1":
#             result = num1 + num2
#         elif option == "2":
#             result = num1 - num2
#         elif option == "3":
#             result = num1 / num2
#         elif option == "4":
#             result = num1 * num2
#         else:
#             result = "Invalid operation"

#     return render_template("index.html", result=result)

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # render main page
    return render_template("index.html")

@app.route("/calc", methods=["POST"])
def calc():
    # this endpoint receives JSON from the front-end and returns the result
    try:
        data = request.get_json()
        op = data.get("op")        # '+', '-', '*', '/'
        a = float(data.get("a"))
        b = float(data.get("b"))

        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            if b == 0:
                return jsonify({"error": "Division by zero"}), 400
            res = a / b
        else:
            return jsonify({"error": "Invalid operator"}), 400

        # return result as JSON
        return jsonify({"result": res})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
