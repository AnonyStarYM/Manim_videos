from manimlib import *
from scipy.fft import fft

class ShowBit(Scene):
    def construct(self):
        dot_0 = (-4,-0.5,0)
        dot_1 = (-3.5,-0.5,0)
        dot_2 = (-3.5,1,0)
        dot_3 = (-2.5,1,0)
        dot_4 = (-2.5,-0.5,0)
        dot_5 = (-2,-0.5,0)

        dot_10 = (-1.5,1,0)
        dot_11 = (-1,1,0)
        dot_12 = (-1,-0.5,0)
        dot_13 = (0,-0.5,0)
        dot_14 = (0,1,0)
        dot_15 = (0.5,1,0)

        line_23 = Line(dot_2, dot_3)
        self.add(line_23)
        mobject_0 = VGroup(
            Line(dot_1, dot_0),
            Line(dot_2, dot_1),
            Line(dot_3, dot_4),
            Line(dot_4, dot_5),
            Tex("1").scale(2).shift(LEFT*3+UP*2)                
        )
        self.play(*[ShowCreation(mob) for mob in mobject_0])
        self.wait()

        line_1213 = Line(dot_12, dot_13)
        self.add(line_1213)
        mobject_1 = VGroup(
            Line(dot_11, dot_10),
            Line(dot_12, dot_11),
            Line(dot_13, dot_14),
            Line(dot_14, dot_15),
            Tex("0").scale(2).shift(LEFT*0.5+UP*2)
        )
        self.play(*[ShowCreation(mob) for mob in mobject_1]) 
        
        self.wait(2)
        Qubit = Text("Qubit", font="serif").scale(1.5).set_color(YELLOW_C).shift(RIGHT*3+UP*2)
        superposition = Tex(r"|\psi\rangle").scale(2).set_color(YELLOW_C).shift(RIGHT*3+UP*0.2)
        self.play(DrawBorderThenFill(Qubit))
        self.play(DrawBorderThenFill(superposition))
        self.wait(2)


class Dice(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }
    def construct(self):
        axes = ThreeDAxes()
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        dice = Group(
            Cube(side_length=1,color=PURPLE_A),
            Tex("1").shift(DOWN*0.5).rotate(axis=RIGHT, angle=90*DEGREES),
            Tex("2").shift(LEFT*0.5).rotate(axis=UP, angle=270*DEGREES),
            Tex("3").shift(RIGHT*0.5).rotate(axis=UP, angle=90*DEGREES),
            Tex("4").shift(UP*0.5).rotate(axis=RIGHT, angle=90*DEGREES).flip(),
            Tex("5").shift(IN*0.5).flip(),
            Tex("6").shift(OUT*0.5),
        )
        self.play(*[ShowCreation(mob) for mob in dice])
        self.wait(3)
        self.play(
            Rotating(dice,angle=12*PI,run_time=5,axis=(1,1,1))
        )
        self.wait(0.5)

        #===============
        mobjects = VGroup(
                Square(fill_opacity=0.6, color=PURPLE, side_length=1).shift(RIGHT*3+DOWN*0.5),
                Tex("5").shift(RIGHT*3+DOWN*0.5)
        ).fix_in_frame()
        self.play(*[GrowFromPoint(mob,mob.get_center()+LEFT*3) for mob in mobjects])
        self.wait(3)

        #================
        superp_1 = Tex(r"|1\rangle+|2\rangle+|3\rangle+|4\rangle+|5\rangle+|6\rangle").scale(1).shift(UP*2).fix_in_frame()
        self.play(GrowFromPoint(superp_1, superp_1.get_center()+DOWN*2))
        self.wait()
        superp_2 = Tex(r"\sqrt{\frac{1}{6}}|1\rangle+\sqrt{\frac{1}{6}}|2\rangle+\sqrt{\frac{1}{6}}|3\rangle+\sqrt{\frac{1}{6}}|4\rangle+\sqrt{\frac{1}{6}}|5\rangle+\sqrt{\frac{1}{6}}|6\rangle").scale(1).shift(UP*2).fix_in_frame()
        self.play(Transform(superp_1, superp_2))
        self.wait()
        self.remove(superp_1)
        superp_3 = Tex(r"|1\rangle+|2\rangle+|3\rangle+|4\rangle+|5\rangle+|6\rangle").scale(1).shift(UP*2).fix_in_frame()
        self.play(Transform(superp_2, superp_3))
        self.wait()

        #================
        q_1 = Text("Why Qubit Exists?", font="serif").scale(1.5).set_color(YELLOW_C).shift(LEFT*4).fix_in_frame()
        self.play(DrawBorderThenFill(q_1))
        self.wait()
        

class LogitGate(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }
    def construct(self):
        axes = ThreeDAxes()
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        #===============
        logitgate = VGroup(
            Square(side_length=1).scale(1.1),
            Tex("f(x)").scale(0.8)
        ).fix_in_frame()
        self.play(*[ShowCreation(mob) for mob in logitgate])
        self.wait()
        logitgate.generate_target()  # copyA自身形成A的target属性
        logitgate.target.shift(RIGHT*3) # 操作A的target
        self.play(MoveToTarget(logitgate))

        dice = Group(
            Cube(side_length=1,color=PURPLE_A),
            Tex("1").shift(DOWN*0.5).rotate(axis=RIGHT, angle=90*DEGREES),
            Tex("2").shift(LEFT*0.5).rotate(axis=UP, angle=270*DEGREES),
            Tex("3").shift(RIGHT*0.5).rotate(axis=UP, angle=90*DEGREES),
            Tex("4").shift(UP*0.5).rotate(axis=RIGHT, angle=90*DEGREES).flip(),
            Tex("5").shift(IN*0.5).flip(),
            Tex("6").shift(OUT*0.5),
        )
        self.play(*[ShowCreation(mob) for mob in dice])
        
        superp_1 = Tex(r"|1\rangle+|2\rangle+|3\rangle+|4\rangle+|5\rangle+|6\rangle").scale(1).shift(UP*2.5).fix_in_frame()
        self.play(GrowFromPoint(superp_1, superp_1.get_center()+DOWN*2))

        curve_0 = CurvedArrow(UP*1.5, UP*1.5+RIGHT*3).flip().rotate(PI).fix_in_frame()
        self.play(ShowCreation(curve_0))
        curve_1 = CurvedArrow(DOWN*1.5+RIGHT*3, DOWN*1.5).flip().rotate(PI).fix_in_frame()
        self.play(ShowCreation(curve_1))

        self.wait()
        superp_2 = Tex(r"|f(1)\rangle+|f(2)\rangle+|f(3)\rangle+|f(4)\rangle+|f(5)\rangle+|f(6)\rangle").scale(1).shift(UP*2.5).fix_in_frame()
        self.play(Transform(superp_1, superp_2))
        self.wait()
        self.remove(superp_1)

        superp_3 = Tex(r"\sqrt{\frac{1}{6}}|1\rangle+\sqrt{\frac{1}{6}}|2\rangle+\sqrt{\frac{1}{6}}|3\rangle+\sqrt{\frac{1}{6}}|4\rangle+\sqrt{\frac{1}{6}}|5\rangle+\sqrt{\frac{1}{6}}|6\rangle").scale(1).shift(UP*2.5).fix_in_frame()
        self.play(GrowFromPoint(superp_3, superp_3.get_center()+DOWN*2.5))
        self.wait()
        superp_4 = Tex(r"\sqrt{\frac{1}{12}}|1\rangle+\sqrt{\frac{3}{12}}|2\rangle+\sqrt{\frac{1}{12}}|3\rangle+\sqrt{\frac{3}{12}}|4\rangle+\sqrt{\frac{1}{12}}|5\rangle+\sqrt{\frac{3}{12}}|6\rangle").scale(1).shift(UP*2.5).fix_in_frame()
        self.play(Transform(superp_3, superp_4))
        self.wait()


class guodu_0(Scene):
    def construct(self): 
        Quantum_text = Text("Quantum Machanics", font="serif").scale(1.5).set_color(YELLOW_C)
        self.play(DrawBorderThenFill(Quantum_text))
        self.wait()
        self.remove(Quantum_text)
        tex_0 = Tex(r"P_1 \times P_2=N").shift(UP*1.5)
        self.play(DrawBorderThenFill(tex_0))
        self.wait(0.3)
        tex_00 = Tex(r"P_1 \times P_2=N").shift(UP*2).set_color(BLUE_C)
        self.play(Transform(tex_0, tex_00))
        self.wait(0.3)
        tex_1 = Tex("g").shift(LEFT*3.8)
        self.play(DrawBorderThenFill(tex_1))
        self.wait(0.3)
        arrow_1 = Group(
            Arrow(start=LEFT*3.8, end=LEFT*2.3),
            Tex("p").shift(LEFT*3.05+UP*0.3)
        )
        self.play(*[ShowCreation(mob) for mob in arrow_1])
        self.wait(0.3)
        tex_2 = Tex(r"g^{p}=m\times N+1").shift(LEFT*0.4)
        self.play(DrawBorderThenFill(tex_2))
        self.wait(0.3)
        arrow_2 = Arrow(start=RIGHT*1.5, end=RIGHT*3)
        self.play(ShowCreation(arrow_2))
        self.wait(0.3)
        tex_3 = Tex(r"g^{\frac{p}{2}}\pm1").shift(RIGHT*4)
        self.play(DrawBorderThenFill(tex_3))
        self.wait(0.3)
        tex_4 = Tex(r"P_1=gcd(g^{\frac{p}{2}}+1,N)").shift(LEFT*2.5+DOWN*1.5)
        self.play(DrawBorderThenFill(tex_4))
        tex_5 = Tex(r"P_2=gcd(g^{\frac{p}{2}}-1,N)").shift(RIGHT*2.5+DOWN*1.5)
        self.play(DrawBorderThenFill(tex_5))
        self.wait(0.3)
        
        
class Shor0(Scene):
    def construct(self): 
        Quantum_text = Text("Shor's Algorithm", font="serif").scale(1.5).set_color(YELLOW_C)
        self.play(DrawBorderThenFill(Quantum_text))
        self.wait(0.3)
        self.remove(Quantum_text)

        t_0 = Tex("x").shift(LEFT*4)
        a_0 = Arrow(start=LEFT*3.8, end=LEFT*2.3)
        self.play(ShowCreation(t_0))
        self.play(ShowCreation(a_0))
        lg_0 = VGroup(
            Square(side_length=1).scale(1.1).shift(LEFT*2),
            Tex(r"g^x").scale(0.8).shift(LEFT*2)
        )
        self.play(*[ShowCreation(mob) for mob in lg_0])
        a_1 = Arrow(start=LEFT*1.7, end=LEFT*0.2)
        self.play(ShowCreation(a_1))
        t_1 = Tex(r"g^x")
        self.play(ShowCreation(t_1))

        a_2 = Arrow(start=RIGHT*0.2, end=RIGHT*1.7)
        self.play(ShowCreation(a_2))
        lg_1 = VGroup(
            Square(side_length=1).scale(1.1).shift(RIGHT*2),
            Tex(r"\bmod N").scale(0.6).shift(RIGHT*2)
        )
        self.play(*[ShowCreation(mob) for mob in lg_1])
        a_3 = Arrow(start=RIGHT*2.3, end=RIGHT*3.8)
        self.play(ShowCreation(a_3))

        t_2 = Tex(r"g^x \bmod N").scale(0.8).shift(RIGHT*4.5)
        self.play(ShowCreation(t_2))
        self.wait(0.3)

        superp_1 = Tex(r"|1\rangle+|2\rangle+|3\rangle+...").scale(0.6).shift(UP*1.5+LEFT*4).set_color(MAROON_B)
        self.play(GrowFromPoint(superp_1, superp_1.get_center()+DOWN*1))
        superp_2 = Tex(r"|1,g^1\rangle+|2,g^2\rangle+|3,g^3\rangle+...").scale(0.6).shift(UP*1.5).set_color(MAROON_B)
        self.play(GrowFromPoint(superp_2, superp_2.get_center()+DOWN*1))
        superp_3 = Tex(r"|1,17\rangle+|2,5\rangle+|3,92\rangle+...").scale(0.6).shift(UP*1.5+RIGHT*4.5).set_color(MAROON_B)
        self.play(GrowFromPoint(superp_3, superp_3.get_center()+DOWN*1))
        t_3 = Tex(r"|p,1\rangle").scale(1.5).shift(UP*2.5+RIGHT*4.5).set_color(RED_C)
        self.play(GrowFromPoint(t_3, t_3.get_center()+DOWN*1))



class rule_0(Scene):
    def construct(self): 
        t_0 = Tex(r"g^x \bmod N = g^{x+p} \bmod N = r")
        self.play(DrawBorderThenFill(t_0))
        self.wait(0.3)
        t_00 = Tex(r"g^x \bmod N = g^{x+p} \bmod N = r").shift(UP*3).set_color(BLUE_C)
        self.play(Transform(t_0, t_00))
        t_1 = Tex(r"g^{p+x} = g^p \times g^x = (m N + 1)(m_1 N + r)").shift(UP*1.5)
        self.play(ShowCreation(t_1))
        t_2 = Tex(r"= m m_1 N^2 + rmN+m_1 N +r").shift(UP*0.5+RIGHT*0.25)
        self.play(ShowCreation(t_2))
        t_3 = Tex(r"= (m m_1 N + rm+m_1) N +r").shift(DOWN*0.5+RIGHT*0.1)
        self.play(ShowCreation(t_3))
        t_4 = Tex(r"= n N +r").shift(DOWN*1.5+LEFT*1.9)
        self.play(ShowCreation(t_4))
        self.wait(0.3)


class periodical(Scene):
    def construct(self):
        superp_1 = Tex(r"|1,17\rangle+|2,5\rangle+|3,92\rangle+...+|1+p,17\rangle+|2+p,5\rangle+|3+p,92\rangle+...").scale(0.8).set_color(GOLD_B)
        self.play(DrawBorderThenFill(superp_1))
        a_1 = Arc(arc_center=[-2.7,0,0], angle=PI, radius=2.4).shift(UP*0.5).set_color(BLUE_C)
        self.play(ShowCreation(a_1))
        a_2 = Arc(arc_center=[-1.1,0,0], angle=PI, radius=2.7).shift(UP*0.5).set_color(TEAL_C)
        self.play(ShowCreation(a_2))
        a_3 = Arc(arc_center=[0.9,0,0], angle=PI, radius=3.1).shift(UP*0.5).set_color(GREEN_C)
        self.play(ShowCreation(a_3))
        self.wait(0.3)

class fourier0(Scene):
    def construct(self):
        axes = Axes((0, 50, 5), (0, 100, 10))
        axes.add_coordinate_labels()
        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        dots0 = Group(
            Dot(color=RED).move_to(axes.c2p(1, 17)),
            Dot(color=RED).move_to(axes.c2p(2, 5)),
            Dot(color=RED).move_to(axes.c2p(3, 92)),
            Dot(color=RED).move_to(axes.c2p(4, 51)),
            Dot(color=RED).move_to(axes.c2p(5, 75)),
            Dot(color=RED).move_to(axes.c2p(6, 55)),
            Dot(color=RED).move_to(axes.c2p(7, 82)),
            Dot(color=RED).move_to(axes.c2p(8, 13)),
            Dot(color=RED).move_to(axes.c2p(9, 17)),
            Dot(color=RED).move_to(axes.c2p(10, 1)),
        )
        self.play(*[FadeIn(mob, scale=0.3) for mob in dots0])

        dots1 = Group(
            Dot(color=ORANGE).move_to(axes.c2p(11, 17)),
            Dot(color=ORANGE).move_to(axes.c2p(12, 5)),
            Dot(color=ORANGE).move_to(axes.c2p(13, 92)),
            Dot(color=ORANGE).move_to(axes.c2p(14, 51)),
            Dot(color=ORANGE).move_to(axes.c2p(15, 75)),
            Dot(color=ORANGE).move_to(axes.c2p(16, 55)),
            Dot(color=ORANGE).move_to(axes.c2p(17, 82)),
            Dot(color=ORANGE).move_to(axes.c2p(18, 13)),
            Dot(color=ORANGE).move_to(axes.c2p(19, 17)),
            Dot(color=ORANGE).move_to(axes.c2p(20, 1)),
        )
        self.play(*[FadeIn(mob, scale=0.3) for mob in dots1])

        dots2 = Group(
            Dot(color=YELLOW_C).move_to(axes.c2p(21, 17)),
            Dot(color=YELLOW_C).move_to(axes.c2p(22, 5)),
            Dot(color=YELLOW_C).move_to(axes.c2p(23, 92)),
            Dot(color=YELLOW_C).move_to(axes.c2p(24, 51)),
            Dot(color=YELLOW_C).move_to(axes.c2p(25, 75)),
            Dot(color=YELLOW_C).move_to(axes.c2p(26, 55)),
            Dot(color=YELLOW_C).move_to(axes.c2p(27, 82)),
            Dot(color=YELLOW_C).move_to(axes.c2p(28, 13)),
            Dot(color=YELLOW_C).move_to(axes.c2p(29, 17)),
            Dot(color=YELLOW_C).move_to(axes.c2p(30, 1)),
        )
        self.play(*[FadeIn(mob, scale=0.3) for mob in dots2])

        dots3 = Group(
            Dot(color=TEAL_B).move_to(axes.c2p(31, 17)),
            Dot(color=TEAL_B).move_to(axes.c2p(32, 5)),
            Dot(color=TEAL_B).move_to(axes.c2p(33, 92)),
            Dot(color=TEAL_B).move_to(axes.c2p(34, 51)),
            Dot(color=TEAL_B).move_to(axes.c2p(35, 75)),
            Dot(color=TEAL_B).move_to(axes.c2p(36, 55)),
            Dot(color=TEAL_B).move_to(axes.c2p(37, 82)),
            Dot(color=TEAL_B).move_to(axes.c2p(38, 13)),
            Dot(color=TEAL_B).move_to(axes.c2p(39, 17)),
            Dot(color=TEAL_B).move_to(axes.c2p(40, 1)),
        )
        self.play(*[FadeIn(mob, scale=0.3) for mob in dots3])

        dots4 = Group(
            Dot(color=PINK).move_to(axes.c2p(41, 17)),
            Dot(color=PINK).move_to(axes.c2p(42, 5)),
            Dot(color=PINK).move_to(axes.c2p(43, 92)),
            Dot(color=PINK).move_to(axes.c2p(44, 51)),
            Dot(color=PINK).move_to(axes.c2p(45, 75)),
            Dot(color=PINK).move_to(axes.c2p(46, 55)),
            Dot(color=PINK).move_to(axes.c2p(47, 82)),
            Dot(color=PINK).move_to(axes.c2p(48, 13)),
            Dot(color=PINK).move_to(axes.c2p(49, 17)),
            Dot(color=PINK).move_to(axes.c2p(50, 1)),
        )
        self.play(*[FadeIn(mob, scale=0.3) for mob in dots4])
        self.wait(0.3)

        t_0 = Tex(r"f=\frac{1}{p}").shift(DOWN*1)
        self.play(DrawBorderThenFill(t_0))
        self.wait(0.3)

        # ===========================================
        self.clear()
        axes_0 = Axes((0, 10),(-1, 1),height=2,width=10)
        axes_0.add_coordinate_labels()
        self.play(Write(axes_0, lag_ratio=0.01, run_time=1))
        sin_graph = axes_0.get_graph(
            lambda x: math.sin(PI*x),
            color=BLUE,
        )
        sin_label = axes_0.get_graph_label(sin_graph, "\\sin(\pi x)")
        self.play(
            ShowCreation(sin_graph),
            FadeIn(sin_label, RIGHT),
        )
        self.remove(sin_label)
        self.play(
            axes_0.animate.scale(0.7).to_corner(UL),
            sin_graph.animate.scale(0.7).to_corner(UL).shift(RIGHT*0.31),
            run_time=1,
        )
        self.wait(0.3)
        t_1 = Tex(r"f=\frac{1}{2}").shift(UP*2.5+RIGHT*2.5)
        self.play(ShowCreation(t_1))

        t_2 = Tex(r"g(f)=\int_{t_1}^{t_2} g(t) e^{-2\pi i ft} dt")
        self.play(DrawBorderThenFill(t_2))

        
class fourier1(Scene):
    def construct(self):
        QFT_text = Text("Quantum Fourier Transform", font="serif").scale(1).set_color(TEAL_A).shift(UP*2.5)
        self.play(DrawBorderThenFill(QFT_text))
        
        superp_1 = Tex(r"|1,17\rangle+|2,5\rangle+|3,92\rangle+...").scale(0.8).shift(LEFT*4)
        self.play(ShowCreation(superp_1))

        a_0 = Arrow(start=LEFT*1.8, end=LEFT*0.3)
        self.play(ShowCreation(a_0))
        lg_0 = VGroup(
            Square(side_length=1).scale(1.1),
            Tex(r"QFT").scale(0.8)
        )
        self.play(*[ShowCreation(mob) for mob in lg_0])
        a_1 = Arrow(start=RIGHT*0.3, end=RIGHT*1.8)
        self.play(ShowCreation(a_1))
        superp_2 = Tex(r"|\frac{1}{p}\rangle").shift(RIGHT*2)
        self.play(ShowCreation(superp_2))

        superp_3 = Tex(r"g^{\frac{p}{2}}\pm1").shift(RIGHT*4).set_color(YELLOW_C)
        self.play(ShowCreation(superp_3))
        superp_4 = Tex(r"P_1=gcd(g^{\frac{p}{2}}+1,N)").shift(RIGHT*4+DOWN*1).set_color(YELLOW_C)
        self.play(ShowCreation(superp_4))
        superp_5 = Tex(r"P_2=gcd(g^{\frac{p}{2}}-1,N)").shift(RIGHT*4+DOWN*2).set_color(YELLOW_C)
        self.play(ShowCreation(superp_5))

        self.wait(0.3)


class End(Scene):
    def construct(self):
        QFT_text = Text("Quantum Supremacy", font="serif").scale(1).set_color(TEAL_A).shift(UP*2)
        self.play(DrawBorderThenFill(QFT_text))

        s_0 = Text("32b6a0daf53397d519d79896bf52214\n5e216fb6ce74416bfe8b92cf6b767373a").scale(0.6)
        self.play(ShowCreation(s_0))
        self.wait()

        s_1 = Text("It's a secret").scale(1.2)
        self.play(FadeTransform(s_0, s_1))
        self.wait()
        self.play(FadeOut(s_1))
        self.play(FadeOut(QFT_text))
        self.wait()


class Start(Scene):
    def construct(self):
        lg_0 = VGroup(
            Square(side_length=1).scale(1.1).shift(LEFT*4),
            Tex(r"Alice").scale(0.6).shift(LEFT*4)
        )
        self.play(*[ShowCreation(mob) for mob in lg_0])
        a_1 = Arrow(start=LEFT*3.7, end=LEFT*2.2)
        self.play(ShowCreation(a_1))
        s_1 = Text("I want to tell you something secret.").scale(0.6)
        self.play(ShowCreation(s_1))

        a_2 = Arrow(start=RIGHT*2.2, end=RIGHT*3.7)
        self.play(ShowCreation(a_2))
        lg_1 = VGroup(
            Square(side_length=1).scale(1.1).shift(RIGHT*4),
            Tex(r"Bob").scale(0.6).shift(RIGHT*4)
        )
        self.play(*[ShowCreation(mob) for mob in lg_1])

        s_2 = Text("32b6a0daf53397d519d79896bf52214\n5e216fb6ce74416bfe8b92cf6b767373a").scale(0.55)
        self.play(FadeTransform(s_1, s_2))

        self.wait()


class RSA(Scene):
    def construct(self):
        s_1 = Tex("RSA").shift(UP*3+LEFT*4)
        self.play(ShowCreation(s_1))
        s_2 = Text("Public Key", font="serif").scale(0.6).shift(UP*3).set_color(TEAL_A)
        self.play(ShowCreation(s_2))
        s_3 = Text("Private Key", font="serif").scale(0.6).shift(UP*2.5+RIGHT*0.05).set_color(BLUE_A)
        self.play(ShowCreation(s_3))

        t_1 = Tex(r"N=P_1 \times P_2").scale(0.7).shift(UP*1+LEFT*3.8)
        self.play(DrawBorderThenFill(t_1))
        t_2 = Tex(r"\phi (N)=(P_1-1)(P_2-1)").scale(0.7).shift(UP*0.5+LEFT*3)
        self.play(DrawBorderThenFill(t_2))

        t_3 = Tex(r"gcd(e,\phi (N))=1").scale(0.7).shift(DOWN*0.5+LEFT*3.6).set_color(TEAL_A)
        self.play(DrawBorderThenFill(t_3))
        s_4 = Tex(r"(N,e)").scale(0.6).shift(UP*3+RIGHT*2).set_color(TEAL_A)
        self.play(ShowCreation(s_4))

        t_4 = Tex(r"ed=1 \bmod \phi (N)").scale(0.7).shift(LEFT*3.5+DOWN*1).set_color(BLUE_A)
        self.play(DrawBorderThenFill(t_4))
        s_5 = Tex(r"(N,d)").scale(0.6).shift(UP*2.5+RIGHT*2).set_color(BLUE_A)
        self.play(ShowCreation(s_5))

        t_5 = Tex(r"Encryption:").scale(0.7).shift(UP*1+RIGHT*1).set_color(GOLD_A)
        self.play(DrawBorderThenFill(t_5))
        t_6 = Tex(r"c=a^e \bmod N").scale(0.7).shift(UP*0.5+RIGHT*1).set_color(GOLD_A)
        self.play(DrawBorderThenFill(t_6))

        t_7 = Tex(r"Decryption:").scale(0.7).shift(DOWN*0.5+RIGHT*1).set_color(GOLD_A)
        self.play(DrawBorderThenFill(t_7))
        t_8 = Tex(r"c^d=a^{ed} \bmod N=a").scale(0.7).shift(DOWN*1+RIGHT*1.4).set_color(GOLD_A)
        self.play(DrawBorderThenFill(t_8))

        t_9 = Tex(r"N=P_1 \times P_2").scale(1.4).shift(UP*1.5+LEFT*3.8).set_color(GOLD_A)
        self.play(FadeTransform(t_1, t_9))

class Reference(Scene):
    def construct(self):
        s_1 = Tex("References").shift(UP*3+LEFT*4)
        self.play(ShowCreation(s_1))
        t_1 = Tex(r"[1]https://zhuanlan.zhihu.com/p/139329165").scale(0.7).shift(UP*1+LEFT*1.1)
        self.play(ShowCreation(t_1))
        t_2 = Tex(r"[2]https://www.youtube.com/watch?v=lvTqbM5Dq4Q").scale(0.7).shift(+LEFT*0.28)
        self.play(ShowCreation(t_2))
        t_3 = Tex(r"[3]https://docs.manim.org.cn/documentation").scale(0.7).shift(DOWN*1+LEFT*1)
        self.play(ShowCreation(t_3))
