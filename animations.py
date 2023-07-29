#!/usr/bin/env python


from manim import *
from manim_fonts import *
# To watch one of these scenes, run the following:
# python --quality m manim -p example_scenes.py SquareToCircle
#
# Use the flag --quality l for a faster rendering at a lower quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have preview of the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the nth animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1920,1080
# for a 1920x1080 video)






class U1PrimitiveTypes(Scene):
    
    # SCRIPT
    '''
    Unit 1, Primitive types. 
    Essentially, they're basic data types that store individual values
    '''


    def construct(self):
        title = Text("Unit 1: Primitive Types", weight="BOLD").shift(UP * 2.2)
        underline = Underline(title, color=WHITE, buff=0.1)
        self.play(FadeIn(title, shift=DOWN), run_time=0.5)
        self.play(Create(underline))

        self.wait(1.8)

        # Create the centered text for primitive_type_desc
        primitive_type_desc = Text(
            "Basic data types that store individual values"
        )
        primitive_type_desc.shift(UP * 0.1 - primitive_type_desc.get_center())
        primitive_type_desc.shift(UP)

        self.play(Write(primitive_type_desc))
        self.wait(2)
        
        example_title = Text("These include:", weight="BOLD")
        example_title.to_corner(UP * 1.7)
        
        transition_group = AnimationGroup (
            FadeOut(title, shift=DOWN), FadeOut(underline, shift=DOWN),
        )
       
        self.play(
            transition_group,
            Transform(primitive_type_desc, example_title),
        )
        
        int_text = Text("int", slant="ITALIC").shift(LEFT* 1.6).shift(UP * 1.8)
        byte_text = Text("byte", slant="ITALIC").shift(LEFT* 1.6).shift(UP * 0.6)
        short_text = Text("short", slant="ITALIC").shift(LEFT* 1.6).shift(DOWN * 0.6)
        long_text = Text("long", slant="ITALIC").shift(LEFT* 1.6).shift(DOWN * 1.8)
        
        float_text = Text("float", slant="ITALIC").shift(RIGHT * 1.3).shift(UP * 1.8)
        double_text = Text("double", slant="ITALIC").shift(RIGHT* 1.3).shift(UP * 0.6)
        char_text = Text("char", slant="ITALIC").shift(RIGHT* 1.3).shift(DOWN * 0.6)
        boolean_text = Text("boolean", slant="ITALIC").shift(RIGHT* 1.3).shift(DOWN * 1.8)
        
        self.play(Write(int_text))
        self.play(Write(byte_text))
        self.play(Write(short_text))
        self.play(Write(long_text))
        
        self.play(Write(float_text))
        self.play(Write(double_text))
        self.play(Write(char_text))
        self.play(Write(boolean_text))
        
        self.wait(2.5)
        
        fadeout_group = AnimationGroup(
            FadeOut(byte_text), FadeOut(short_text)
        )
        self.wait(1.2)
        self.play(
            fadeout_group,
        )
        
        self.play(
            ApplyMethod(boolean_text.move_to, byte_text.get_center()),
            ApplyMethod(long_text.move_to, short_text.get_center()),
            )
        
        # int explanation
        
        '''
        the int data type, which stands for "integer" represents whole numbers. 
        It's used to store numeric values without fractional parts. 
        The int data type has a default value of 0 and is 32 bits in size.
        '''
        
       
        desc = Text("short for integer, stores whole numbers")
        
        def_pos_tl = UP * 2.3 + LEFT * 5.8
        
        
        
        
        
        hyphen_text = Text("-")
        
        self.wait(1.4)
        
        self.play(
        
        ApplyMethod(int_text.move_to, def_pos_tl ),
        FadeOut(float_text),
        FadeOut(long_text),
        FadeOut(double_text),
        FadeOut(char_text),
        FadeOut(boolean_text),
        FadeOut(primitive_type_desc),
        )
        
        hyphen_text.next_to(int_text, RIGHT)
        self.play(FadeIn(hyphen_text, run_time=0.3))
        desc.next_to(hyphen_text, RIGHT)
        self.wait(0.2)
        self.play(Write(desc))
        
        # S: In the real world, integers would represent any real number that's not equal to infinity
     
        constantN = Text("n", slant=ITALIC)
        left_value= MathTex(r"-2^{31}")
        left_operator = MathTex(r"\leq")
        right_operator = MathTex(r"\leq")
        right_value = MathTex(r"2^{31} - 1")
        
        restraintsGroup = VGroup(left_value, left_operator, constantN, right_operator, right_value)
        right_operator.next_to(right_value, LEFT, buff=0.32) # Node for translating x y pos
        constantN.next_to(right_operator, LEFT, buff=0.32)
        left_operator.next_to(constantN, LEFT, buff=0.32)
        left_value.next_to(left_operator, LEFT, buff=0.32)
        
        restraintsGroup.shift(RIGHT * 1.5)
        self.play(Write(restraintsGroup))
        
        self.wait(6.7)
        
        
        long_text.move_to(def_pos_tl)
        self.play(FadeOut(desc),
                  FadeOut(hyphen_text),
                  FadeOut(int_text),
                  FadeIn(long_text),
                  FadeOut(restraintsGroup))
        hyphen_text.next_to(long_text, RIGHT)
        self.play(FadeIn(hyphen_text))
        desc = Text("stores larger whole numbers when a\nlarger range is needed compared to int")
        desc.next_to(hyphen_text, RIGHT)
        self.play(Write(desc))
        
        self.wait(3.7)
        
        constantN = Text("n", slant=ITALIC)
        left_value= MathTex(r"-2^{63}")
        left_operator = MathTex(r"\leq")
        right_operator = MathTex(r"\leq")
        right_value = MathTex(r"2^{63} - 1")
        
        restraintsGroup = VGroup(left_value, left_operator, constantN, right_operator, right_value)
        right_operator.next_to(right_value, LEFT, buff=0.32) # Node for translating x y pos
        constantN.next_to(right_operator, LEFT, buff=0.32)
        left_operator.next_to(constantN, LEFT, buff=0.32)
        left_value.next_to(left_operator, LEFT, buff=0.32)
        
        restraintsGroup.shift(RIGHT * 1.7)
        
        self.play(Write(restraintsGroup))
        
        
        self.wait(6.7)
        
    
        self.play(FadeOut(long_text),FadeOut(hyphen_text), FadeOut(desc), FadeOut(restraintsGroup))
        desc = Text("stores numbers with decimals")
        ampersand = Text("&")
        float_text.move_to(def_pos_tl + RIGHT * 0.08)
        self.play(FadeIn(float_text))
        ampersand.next_to(float_text, RIGHT)
        ampersand.shift(UP * 0.08)
        nextToAmpersandR = ampersand.get_center() + RIGHT * 1.5
        double_text.move_to(nextToAmpersandR)
        self.play(Write(ampersand),
                  FadeIn(double_text))
        hyphen_text.next_to(double_text, RIGHT)
        self.play(Write(hyphen_text))
        desc.next_to(hyphen_text, RIGHT)
        self.play(Write(desc))
        
        self.wait(1.3)
        self.play(FadeOut(ampersand), FadeOut(hyphen_text), FadeOut(desc))
        belowFloatTxtPos = float_text.get_center() + DOWN * 1.4
        self.play(ApplyMethod(double_text.move_to, belowFloatTxtPos))
        
        hyphen_text2 = Text("-")
        hyphen_text.next_to(float_text, RIGHT)
        hyphen_text2.next_to(double_text, RIGHT)
        self.play(Write(hyphen_text2), Write(hyphen_text))
        
        floatSigVal = Text("Appox. 7 significant decimal places")
        doubleSigVal = Text("Appox. 15 significant decimal places")
        floatSigVal.next_to(hyphen_text, RIGHT, buff = 0.3)
        doubleSigVal.next_to(hyphen_text2, RIGHT, buff = 0.3)
       
        self.play(Write(floatSigVal))
        self.wait(2.2)
        self.play(Write(doubleSigVal))
        self.wait(2.2 )
        char_text.move_to(def_pos_tl + RIGHT)
        self.play(FadeOut(hyphen_text),
                  FadeOut(hyphen_text2),
                  FadeOut(floatSigVal),
                  FadeOut(doubleSigVal),
                  FadeOut(float_text),
                  FadeOut(double_text),
                  FadeIn(char_text))
        hyphen_text.next_to(char_text, RIGHT, buff = 0.2)
        desc = Text("represent a single character ")
        desc.next_to(hyphen_text, RIGHT, buff = 0.2)
        self.play(Write(hyphen_text), Write(desc))
        
        # There are many examples of characters
        self.wait(1.6)
        self.play(FadeOut(char_text),
                  FadeOut(hyphen_text),
                  FadeOut(desc),)
        
        boolean_text.move_to(def_pos_tl)
        boolean_text.shift(RIGHT * 1.3)
        self.play(FadeIn(boolean_text))
        hyphen_text.next_to(boolean_text, RIGHT, buff = 0.2)
        desc = Text("a status representing true or false")
        desc.next_to(hyphen_text, RIGHT, buff=0.2)
        self.play(Write(hyphen_text), Write(desc))
        
        
        lightbulb_on = ImageMobject("lightbulbon.png").scale(1.2)
        lightbulb_off = ImageMobject("lightbulboff.png")

        # Position the lightbulbs on the screen
        lightbulbPos = DOWN * 0.8
        lightbulb_on.shift(lightbulbPos).shift(UP * 0.28 + RIGHT * 0.03)
        
        lightbulb_off.shift(lightbulbPos)

        # Add the lightbulbs to the scene
        self.wait(2)
        self.play(FadeIn(lightbulb_on))
        self.wait(1)
        self.remove(lightbulb_on) 
        self.add(lightbulb_off)
        
        self.wait(1)
        


        






        
        
        
        
        
        
        
class ints1(Scene):
    # Whole number computations
    def construct(self):
        number_line = NumberLine(x_range=[-5, 5], length=10, unit_size=1, include_numbers=False).shift(UP * 0.6)

        # Manually create the number labels and replace the labels at -5 and 5
        number_labels = VGroup(
            Integer(-5).next_to(number_line.n2p(-5), DOWN, buff=0.2),
            Integer(-4).next_to(number_line.n2p(-4), DOWN, buff=0.2),
            Integer(-3).next_to(number_line.n2p(-3), DOWN, buff=0.2),
            Integer(-2).next_to(number_line.n2p(-2), DOWN, buff=0.2),
            Integer(-1).next_to(number_line.n2p(-1), DOWN, buff=0.2),
            Integer(0).next_to(number_line.n2p(0), DOWN, buff=0.2),
            Integer(1).next_to(number_line.n2p(1), DOWN, buff=0.2),
            Integer(2).next_to(number_line.n2p(2), DOWN, buff=0.2),
            Integer(3).next_to(number_line.n2p(3), DOWN, buff=0.2),
            Integer(4).next_to(number_line.n2p(4), DOWN, buff=0.2),
            Integer(5).next_to(number_line.n2p(5), DOWN, buff=0.2),
            
        )

        # Store the number labels to be faded out in a separate group
        numbers_to_fade_out = VGroup(
          
            number_labels[1],
            number_labels[2],
            number_labels[3],
            number_labels[4],
            number_labels[6],
            number_labels[7],
            number_labels[8],
            number_labels[9],
            
     
        )
        whole_numbers = list(range(-5, 6))
        red_dots = [Dot(number_line.n2p(number), color=RED, radius = 0.11) for number in whole_numbers]
        red_dots_group = VGroup(*red_dots)

        # Add the number line and the custom number labels to the scene
        self.play(
            Create(number_line),
            *[Create(label) for label in number_labels],
            Create(red_dots_group)
        )

        # Wait for a moment
        self.wait(0.5)
        self.play(FadeOut(red_dots_group))

        # Fade out the number labels -5, -4, -3, -2, -1, 1, 2, 3, 4, and 5
        self.play(FadeOut(numbers_to_fade_out))
      
        self.wait(0.3)
        
        neg_int_range = MathTex(r"-2^{31}").next_to(number_line.n2p(-5), DOWN, buff=0.2)
        pos_int_range = MathTex(r"2^{31}-1").next_to(number_line.n2p(5), DOWN, buff=0.2)
        
       
        self.play(
                Transform(number_labels[0],neg_int_range),
                Transform(number_labels[10],pos_int_range),
                )
        
        
        red_dots = [Dot(number_line.n2p(number), color=RED, radius = 0.11) for number in [-5, 5]]
        red_dots_group = VGroup(*red_dots)
        self.play(Create(red_dots_group))
        self.wait(0.7)
        self.play(FadeOut(red_dots_group))

        

        # Fade out the brace and its label
        # self.play(FadeOut(brace), FadeOut(brace_label))

        self.play(
                  FadeOut(number_line),
                  FadeOut(number_labels[0]),
                  FadeOut(number_labels[5]),
                  FadeOut(number_labels[10],))
        
        
        with RegisterFont("Source Code Pro") as fonts:
            int1=Text("int",font=fonts[0], color="#4CC8AF")
            x_var = Text("x", font=fonts[0], color="#9CDCFD")
            eqSign4x = Text("=", font=fonts[0])
            eight_text=Text("8", font=fonts[0], color="#B5CEA8")
            semicolonForEight = Text(";")
            int2=Text("int",font=fonts[0], color="#4CC8AF")
            y_var = Text("y", font=fonts[0], color="#9CDCFD")
            eqSign4y = Text("=", font=fonts[0])
            nine_text=Text("9", font=fonts[0], color="#B5CEA8")
            semicolonForNine = Text(";")
            
            int3=Text("int",font=fonts[0], color="#4CC8AF")
            result_var = Text("result", font=fonts[0], color="#9CDCFD")
            eqSign4result = Text("=", font=fonts[0])
            xOfxplusy=Text("x", font=fonts[0], color="#9CDCFD")
            plusOfxplusy=Text("+", font=fonts[0])
            yOfxplusy=Text("y", font=fonts[0], color="#9CDCFD")
            semicolonForxplusy = Text(";")
             
            int1.shift(UP * 2.4 + LEFT * 4.7)
            int2.shift(UP * 1.3 + LEFT * 4.7)
            int3.shift(UP * 0.2 + LEFT * 4.7)
            
            x_var.next_to(int1, RIGHT, buff= 0.35)
            x_var.shift(DOWN * 0.05)
            eqSign4x.next_to(x_var, RIGHT, buff = 0.35)
            eight_text.next_to(eqSign4x, RIGHT, buff = 0.35)
            y_var.next_to(int2, RIGHT, buff=0.35)
            y_var.shift(DOWN * 0.13)
            eqSign4y.next_to(y_var, RIGHT, buff=0.35)
            eqSign4y.shift(UP*0.09)
            nine_text.next_to(eqSign4y, RIGHT, buff=0.35)
            
            result_var.next_to(int3, RIGHT, buff=0.35)
            
            eqSign4result.next_to(result_var, RIGHT, buff=0.35)
            xplusy = VGroup(xOfxplusy, plusOfxplusy, yOfxplusy)
            plusOfxplusy.next_to(xOfxplusy, RIGHT, buff=0.35)
            yOfxplusy.next_to(plusOfxplusy, RIGHT, buff=0.35)
            yOfxplusy.shift(DOWN * 0.08)
            xplusy.next_to(eqSign4result, RIGHT, buff=0.35)
            xplusy.shift(DOWN*0.09)
            
            semicolonForEight.next_to(eight_text, RIGHT, buff = 0.2)
            semicolonForNine.next_to(nine_text, RIGHT, buff = 0.2)
            semicolonForxplusy.next_to(xplusy, RIGHT, buff = 0.2)
            
            self.play(Write(int1),
                      Write(x_var),
                      Write(eqSign4x),
                      )
            
            self.wait(1)
            
            self.play(Write(int2),
                      Write(y_var),
                      Write(eqSign4y),
                      )
            
            self.wait(1)
            
            self.play(Write(eight_text), Write(semicolonForEight), run_time=0.4)
            self.play(Write(nine_text),Write(semicolonForNine), run_time=0.4)
            self.wait(2.4) #3.2
            self.play(Write(int3), run_time=0.7)
            self.wait(0.5)
            self.play(Write(result_var),
                      Write(eqSign4result))
            self.wait(0.9)
            self.play(Write(xplusy),
                      Write(semicolonForxplusy))
            
            systemOfprintfunc = Text("System",font=fonts[0], color="#4ABDA6")
            outOfprintfunc = Text("out",font=fonts[0], color="#4FC1FF")
            printOfprintfunc = Text("println",font=fonts[0], color="#DCDCAA")
            firstperiod = Text(".",font=fonts[0])
            secondperiod = Text(".",font=fonts[0])
            openingparenthesis = Text("(",font=fonts[0], color="#4FC1FF")
            closingparenthesis = Text(")",font=fonts[0], color="#4FC1FF")
            firstperiod.next_to(systemOfprintfunc, RIGHT)
            firstperiod.shift(DOWN * 0.1)
            outOfprintfunc.next_to(firstperiod, RIGHT)
            outOfprintfunc.shift(UP * 0.17)
            secondperiod.next_to(outOfprintfunc, RIGHT)
            secondperiod.shift(DOWN * 0.17)
            printOfprintfunc.next_to(secondperiod, RIGHT)
            printOfprintfunc.shift(UP * 0.17)
            semicolonForPrint = Text(";")
            
            
            eight=Text("8", font=fonts[0], color="#9CDCFD")
            plus=Text("+", font=fonts[0])
            nine=Text("9", font=fonts[0], color="#9CDCFD")

            result_var2 = Text("result", font=fonts[0], color="#9CDCFD")
            
            
            printfunc = VGroup(systemOfprintfunc, firstperiod, outOfprintfunc, secondperiod, printOfprintfunc)
            printfunc.shift(DOWN * 0.9 + LEFT * 4)
            
            openingparenthesis.next_to(printOfprintfunc, RIGHT)
            result_var2.next_to(openingparenthesis, RIGHT)
            closingparenthesis.next_to(result_var2)
            semicolonForPrint.next_to(closingparenthesis, RIGHT)
            
            
            
            
            
            
           
            self.play(Write(printfunc), run_time=0.4)
            self.play(Write(openingparenthesis), Write(closingparenthesis), Write(result_var2), Write(semicolonForPrint))
            start_point = DOWN * 1.3 + LEFT * 5.2
            end_point = DOWN * 2 + LEFT * 4.5
            arc = CurvedArrow(start_point, end_point)
            self.play(Create(arc), run_time=0.2)
            seventeen = Text("17").move_to(end_point + RIGHT)
            self.play(Write(seventeen), run_time = 0.4)
            
            self.wait(1)
            
            eight.next_to(openingparenthesis, RIGHT * 0.2)
            plus.next_to(eight, RIGHT, buff=0.35)
            nine.next_to(plus, RIGHT, buff=0.35)
    
            # closingparenthesis.next_to(yOfxplusy2, RIGHT, buff=0.35)
            # closingparenthesis.shift(UP * 0.08)
            expression8plus9 = VGroup(eight, plus, nine)
            expression8plus9.shift(RIGHT * 0.3)
            rightofnine = nine.get_center() + RIGHT * 0.6
            rightofclosingparenthesis = closingparenthesis.get_center() + LEFT * 0.1
            self.play(Transform(result_var2, expression8plus9),
                      ApplyMethod(closingparenthesis.move_to, rightofnine),
                      ApplyMethod(semicolonForPrint.move_to, rightofclosingparenthesis))
            
            self.wait()
        
      





        
# Examples @ https://docs.manim.community/en/stable/examples.html
