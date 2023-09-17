from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
WRITE_STYLE = ('Arial', 20, 'italic')

class QuizzInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, padx= 20, pady=20)

        self.scoreboard = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg='white', font=WRITE_STYLE)
        self.scoreboard.grid(column=1, row=0)

        self.true_button_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_image,
                                command=self.true_button_pressed,
                                highlightthickness=0)
        self.true_button.grid(column=0,row=3)

        self.false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_image,
                                command=self.false_button_pressed,
                                highlightthickness=0)
        self.false_button.grid(column=1,row=3)

        self.canvas = Canvas(height=250, width=300)
        self.canvas.grid(column=0,row=1, columnspan=2, padx=20, pady=20)
        
        self.question_text = self.canvas.create_text(150, 125,
                                                    text="Questions",
                                                    font=('Arial',10, 'bold'),
                                                    fill=THEME_COLOR,
                                                    width=280)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        try:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        except IndexError:
            messagebox.showinfo(title="Game finished", message=f"Final score was {self.quiz.score}/10\nPlay another game?")
            self.window.destroy()

    def true_button_pressed(self):
        if self.quiz.check_answer("true") == 'true':
            self.give_feedback("green")
        else:
            self.give_feedback("red")

    def false_button_pressed(self):
        if self.quiz.check_answer("false") == 'false':
            self.give_feedback("green")
        else: 
            self.give_feedback("red")

    def give_feedback(self, color):
        self.scoreboard.config(text=f'Score: {self.quiz.score}')
        self.canvas.config(bg=color)
        self.canvas.after(1000, self.get_next_question)