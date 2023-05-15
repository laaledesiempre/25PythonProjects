words={
    "caballo":""
}

"""
   0
  /|\\
  / \\

"""
current_word=""
class man_stages:
    failures=0
    current_head=""" """
    current_body="""   """
    current_legs="""   """
    def failure(self):
        self.failures+=1
        if self.failures==1:
            self.current_head="""0"""
        elif self.failures==2:
            self.current_body=""" | """
        elif self.failures==3:
            self.current_body="""/| """
        elif self.failures==4:
            self.current_body="""/|\\"""
        elif self.failures==5:
            self.current_legs="""/  """
        elif self.failures==6:
            self.current_legs="""/ \\"""
    def reset(self):
        current_head=""" """
        current_body="""   """
        current_legs="""   """
stickman= man_stages()
display=f"""
   |
   |
  {stickman.current_head}
 {stickman.current_body}
 {stickman.current_legs}

 
"""