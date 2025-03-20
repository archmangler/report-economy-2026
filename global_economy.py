from manim import *
import numpy as np

class GlobalEconomyPresentation(Scene):
    def construct(self):
        # Configuration
        self.camera.background_color = "#1C1C1C"
        
        # Title slide
        self.create_title_slide()
        self.wait(2)
        
        # Introduction animation
        self.create_intro_animation()
        self.wait(1)
        
        # GDP Projections
        self.show_gdp_projections()
        self.wait(1)
        
        # Global Trade Analysis
        self.show_global_trade()
        self.wait(1)
        
        # Technology Impact
        self.show_tech_impact()
        self.wait(1)
        
        # Conclusion
        self.show_conclusion()
        self.wait(2)

    def create_title_slide(self):
        title = Text("The Global Economy in 2026", font_size=60)
        subtitle = Text("Projections and Trends", font_size=40)
        subtitle.next_to(title, DOWN)
        
        group = VGroup(title, subtitle)
        
        self.play(
            Write(title, run_time=2),
            FadeIn(subtitle, run_time=2)
        )
        self.play(group.animate.scale(0.8).to_corner(UP))

    def create_intro_animation(self):
        # Create 3D globe
        sphere = Sphere(radius=2, resolution=(32, 32))
        sphere.set_color(BLUE_E)
        
        # Add rotation animation
        self.play(
            Create(sphere),
            Rotate(sphere, angle=2*PI, axis=UP, run_time=5)
        )
        self.play(FadeOut(sphere))

    def show_gdp_projections(self):
        # Create animated bar chart with expanded dataset
        data = {
            # Major Economies
            "USA": [21, 23, 25],
            "China": [16, 19, 22],
            "Japan": [4.8, 5.0, 5.2],
            "Germany": [4.2, 4.4, 4.6],
            "India": [3.2, 3.8, 4.5],
            
            # Emerging Economies
            "Russia": [1.8, 2.0, 2.3],
            "Brazil": [1.6, 1.8, 2.1],
            "Turkiye": [0.9, 1.1, 1.3],
            "Kazakhstan": [0.2, 0.25, 0.3],
            
            # ASEAN Economies
            "Indonesia": [1.2, 1.4, 1.6],
            "Thailand": [0.5, 0.6, 0.7],
            "Singapore": [0.4, 0.45, 0.5],
            "Malaysia": [0.4, 0.45, 0.5],
            "Vietnam": [0.3, 0.4, 0.5],
            "Cambodia": [0.03, 0.04, 0.05]
        }
        
        # Chart 1: Major Economies
        major_economies = {k: data[k] for k in ["USA", "China", "Japan", "Germany", "India"]}
        chart1 = BarChart(
            values=[major_economies[country][0] for country in major_economies.keys()],
            bar_names=list(major_economies.keys()),
            y_range=[0, 30, 5],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36},
            label_constructor=Text
        )
        
        title1 = Text("Major Economies GDP (Trillion USD)", font_size=40)
        title1.to_edge(UP)
        
        # Chart 2: Emerging Economies
        emerging_economies = {k: data[k] for k in ["Russia", "Brazil", "Turkiye", "Kazakhstan"]}
        chart2 = BarChart(
            values=[emerging_economies[country][0] for country in emerging_economies.keys()],
            bar_names=list(emerging_economies.keys()),
            y_range=[0, 5, 1],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 36},
            label_constructor=Text
        )
        
        title2 = Text("Emerging Economies GDP (Trillion USD)", font_size=40)
        title2.to_edge(UP)

        # Chart 3: ASEAN Economies
        asean_economies = {k: data[k] for k in ["Indonesia", "Thailand", "Singapore", 
                                               "Malaysia", "Vietnam", "Cambodia"]}
        chart3 = BarChart(
            values=[asean_economies[country][0] for country in asean_economies.keys()],
            bar_names=list(asean_economies.keys()),
            y_range=[0, 2, 0.2],
            y_length=6,
            x_length=10,
            x_axis_config={"font_size": 32},
            label_constructor=Text
        )
        
        title3 = Text("ASEAN Economies GDP (Trillion USD)", font_size=40)
        title3.to_edge(UP)

        # Animation sequence for Chart 1: Major Economies
        self.play(
            Create(chart1),
            Write(title1)
        )
        
        for year_idx in range(1, 3):
            new_values = [major_economies[country][year_idx] for country in major_economies.keys()]
            self.play(chart1.animate.change_bar_values(new_values))
            self.wait(1)
        
        # Transition to Chart 2: Emerging Economies
        self.play(
            FadeOut(chart1),
            FadeOut(title1)
        )
        
        self.play(
            Create(chart2),
            Write(title2)
        )
        
        for year_idx in range(1, 3):
            new_values = [emerging_economies[country][year_idx] for country in emerging_economies.keys()]
            self.play(chart2.animate.change_bar_values(new_values))
            self.wait(1)

        # Transition to Chart 3: ASEAN Economies
        self.play(
            FadeOut(chart2),
            FadeOut(title2)
        )
        
        self.play(
            Create(chart3),
            Write(title3)
        )
        
        for year_idx in range(1, 3):
            new_values = [asean_economies[country][year_idx] for country in asean_economies.keys()]
            self.play(chart3.animate.change_bar_values(new_values))
            self.wait(1)
        
        # Final cleanup
        self.play(
            FadeOut(chart3),
            FadeOut(title3)
        )

    def show_global_trade(self):
        # Create line graph for trade volumes
        axes = Axes(
            x_range=[2022, 2026, 1],
            y_range=[0, 100, 20],
            axis_config={"include_tip": True}
        )
        
        trade_data = [(2022, 40), (2023, 50), (2024, 65), (2025, 80), (2026, 95)]
        trade_line = axes.plot_line_graph(
            x_values=[point[0] for point in trade_data],
            y_values=[point[1] for point in trade_data]
        )
        
        title = Text("Global Trade Volume Index", font_size=40)
        title.to_edge(UP)
        
        self.play(
            Create(axes),
            Create(trade_line),
            Write(title)
        )

    def show_tech_impact(self):
        # Create circular diagram for tech sectors
        sectors = ["AI", "Blockchain", "IoT", "Cloud", "5G"]
        circles = VGroup(*[
            Circle(radius=0.5).set_fill(color=BLUE, opacity=0.5)
            for _ in sectors
        ]).arrange_in_grid(rows=2, cols=3, buff=1)
        
        labels = VGroup(*[
            Text(sector, font_size=24).move_to(circle)
            for sector, circle in zip(sectors, circles)
        ])
        
        title = Text("Technology Impact on Economy", font_size=40)
        title.to_edge(UP)
        
        self.play(
            Create(circles),
            Write(labels),
            Write(title)
        )
        
        # Pulse animation for each sector
        for circle in circles:
            self.play(
                circle.animate.scale(1.2),
                rate_func=there_and_back,
                run_time=0.5
            )

    def show_conclusion(self):
        conclusions = [
            "• Continued digital transformation",
            "• Shift in economic power",
            "• Sustainable growth focus",
            "• Innovation-driven markets"
        ]
        
        title = Text("Key Takeaways", font_size=40)
        title.to_edge(UP)
        
        points = VGroup(*[
            Text(point, font_size=32)
            for point in conclusions
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        
        points.next_to(title, DOWN, buff=1)
        
        self.play(Write(title))
        for point in points:
            self.play(
                Write(point),
                run_time=1
            )
