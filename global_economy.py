from manim import *
import numpy as np

class GlobalEconomyPresentation(Scene):
    def construct(self):
        # Configuration
        self.camera.background_color = "#1C1C1C"
        
        # Main title position configuration
        MAIN_TITLE_BUFF = 1.5  # Increased buffer space for main title
        
        # Title slide
        self.create_title_slide()
        self.wait(2)
        
        # Clear the title before proceeding
        self.clear()
        
        # Introduction animation
        self.create_intro_animation()
        self.wait(1)
        
        # GDP Projections with adjusted positioning
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
        subtitle.next_to(title, DOWN, buff=0.5)
        
        group = VGroup(title, subtitle)
        group.move_to(ORIGIN)  # Center the group
        
        self.play(
            Write(title, run_time=2),
            FadeIn(subtitle, run_time=2)
        )

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
        # Reorganized data structure
        data = {
            # Major Global Economies
            "USA": [
                [21.0, 23.0, 25.0],  # GDP Nominal
                [21.5, 23.5, 25.5],  # GDP PPP
                [63.0, 68.0, 73.0]   # GDP per capita
            ],
            "China": [
                [16.0, 19.0, 22.0],
                [27.0, 30.0, 33.0],
                [11.5, 13.0, 15.0]
            ],
            "EU": [
                [17.0, 18.0, 19.0],
                [20.0, 21.0, 22.0],
                [37.0, 39.0, 41.0]
            ],
            "India": [
                [3.2, 3.8, 4.5],
                [11.3, 12.5, 13.8],
                [2.3, 2.7, 3.1]
            ],
            "Russia": [
                [1.8, 2.0, 2.3],
                [4.5, 4.8, 5.1],
                [12.5, 13.5, 14.5]
            ],
            "Brazil": [
                [1.6, 1.8, 2.1],
                [3.4, 3.7, 4.0],
                [7.5, 8.2, 9.0]
            ],
            
            # ASEAN Economies
            "Indonesia": [
                [1.2, 1.4, 1.6],
                [3.8, 4.2, 4.6],
                [4.3, 4.8, 5.3]
            ],
            "Thailand": [
                [0.5, 0.6, 0.7],
                [1.4, 1.5, 1.6],
                [7.2, 7.8, 8.4]
            ],
            "Singapore": [
                [0.4, 0.45, 0.5],
                [0.6, 0.65, 0.7],
                [72.0, 76.0, 80.0]
            ],
            "Malaysia": [
                [0.4, 0.45, 0.5],
                [1.0, 1.1, 1.2],
                [12.0, 13.0, 14.0]
            ],
            "Vietnam": [
                [0.3, 0.4, 0.5],
                [1.2, 1.4, 1.6],
                [3.1, 3.5, 3.9]
            ],
            "Cambodia": [
                [0.03, 0.04, 0.05],
                [0.08, 0.09, 0.1],
                [1.8, 2.0, 2.2]
            ]
        }

        def create_single_metric_chart(economies, metric_index, metric_info, region_title):
            metric_name, color, y_range = metric_info
            
            # Create section title with region
            section_title = Text(f"{region_title}: {metric_name} GDP", font_size=48)
            section_title.to_edge(UP, buff=0.5)
            
            # Create subtitle with metric description
            descriptions = {
                "Nominal": "Market exchange rate based GDP",
                "PPP": "Purchasing Power Parity adjusted GDP",
                "Per Capita": "Average economic output per person"
            }
            subtitle = Text(descriptions[metric_name], font_size=28)
            subtitle.next_to(section_title, DOWN, buff=0.3)
            
            # Create chart
            values = [economies[country][metric_index][0] for country in economies.keys()]
            chart = BarChart(
                values=values,
                bar_names=list(economies.keys()),
                y_range=y_range,
                y_length=5,
                x_length=10,
                x_axis_config={"font_size": 32},
                bar_colors=[color] * len(economies)
            ).scale(0.9)
            
            # Position chart
            chart.next_to(subtitle, DOWN, buff=0.8)
            
            # Create value labels
            def create_value_labels(values, unit):
                labels = VGroup()
                for bar, value in zip(chart.bars, values):
                    if unit == "T":
                        label_text = f"${value:.1f}T"
                    else:
                        label_text = f"${value:.1f}K"
                    label = Text(label_text, font_size=24)
                    label.next_to(bar, UP, buff=0.2)
                    labels.add(label)
                return labels
            
            # Year indicator
            year_label = Text("2024", font_size=36)
            year_label.to_edge(RIGHT, buff=1).to_edge(UP, buff=1)
            
            # Animation sequence
            self.play(Write(section_title), run_time=2)
            self.play(Write(subtitle), run_time=2)
            self.wait(1)
            
            self.play(
                Create(chart),
                Write(year_label),
                run_time=3
            )
            
            # Initial value labels
            value_labels = create_value_labels(values, "T" if metric_index != 2 else "K")
            self.play(Write(value_labels), run_time=2)
            self.wait(2)
            
            # Animate through years
            years = [2025, 2026]
            for year_idx, year in enumerate(years, 1):
                new_year_label = Text(str(year), font_size=36)
                new_year_label.move_to(year_label)
                
                new_values = [economies[country][metric_index][year_idx] 
                            for country in economies.keys()]
                new_value_labels = create_value_labels(new_values, "T" if metric_index != 2 else "K")
                
                self.play(
                    Transform(year_label, new_year_label),
                    chart.animate.change_bar_values(new_values),
                    Transform(value_labels, new_value_labels),
                    run_time=5
                )
                self.wait(3)
            
            # Cleanup
            self.play(
                *[FadeOut(mob) for mob in [
                    section_title, subtitle, chart, year_label, value_labels
                ]],
                run_time=2
            )
            self.wait(1)

        # Show Major Economies
        major_economies = {k: data[k] for k in ["USA", "China", "EU", "India", "Russia", "Brazil"]}
        
        # Show each metric for Major Economies
        for metric_idx, metric_info in enumerate([
            ("Nominal", BLUE, [0, 30, 5]),
            ("PPP", GREEN, [0, 35, 5]),
            ("Per Capita", RED, [0, 80, 10])
        ]):
            create_single_metric_chart(
                major_economies,
                metric_idx,
                metric_info,
                "Major Global Economies"
            )

        # Show ASEAN Economies
        asean_economies = {k: data[k] for k in [
            "Indonesia", "Thailand", "Singapore", "Malaysia", "Vietnam", "Cambodia"
        ]}
        
        # Show each metric for ASEAN Economies
        for metric_idx, metric_info in enumerate([
            ("Nominal", BLUE, [0, 2, 0.2]),
            ("PPP", GREEN, [0, 5, 0.5]),
            ("Per Capita", RED, [0, 85, 10])
        ]):
            create_single_metric_chart(
                asean_economies,
                metric_idx,
                metric_info,
                "ASEAN Economies"
            )

    def show_global_trade(self):
        # Create section title
        section_title = Text("Global Trade Analysis", font_size=48)
        section_title.to_edge(UP, buff=0.5)
        
        # Create axes with adjusted position
        axes = Axes(
            x_range=[2022, 2026, 1],
            y_range=[0, 100, 20],
            axis_config={"include_tip": True},
            x_length=9,
            y_length=5,
        ).scale(0.9)
        
        # Move axes down to leave room for titles
        axes.next_to(section_title, DOWN, buff=1.5)
        
        # Create labels
        x_label = Text("Year", font_size=24)
        y_label = Text("Trade Volume Index", font_size=24)
        
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3).rotate(90 * DEGREES)
        
        # Create chart title
        chart_title = Text("Global Trade Volume Index (2022-2026)", font_size=36)
        chart_title.next_to(section_title, DOWN, buff=0.3)
        
        trade_data = [(2022, 40), (2023, 50), (2024, 65), (2025, 80), (2026, 95)]
        
        # Create points
        dots = VGroup(*[
            Dot(axes.coords_to_point(x, y))
            for x, y in trade_data
        ])
        
        # Create line graph
        line_graph = VMobject()
        line_graph.set_points_smoothly([
            axes.coords_to_point(x, y)
            for x, y in trade_data
        ])
        line_graph.set_color(BLUE)
        
        # Create value labels
        value_labels = VGroup(*[
            Text(f"{y}", font_size=20).next_to(
                axes.coords_to_point(x, y), UP, buff=0.2
            )
            for x, y in trade_data
        ])
        
        # Animation sequence
        self.play(Write(section_title))
        self.play(Write(chart_title))
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Animate dots and lines
        self.play(Create(dots))
        self.play(Create(line_graph))
        self.play(Write(value_labels))
        
        self.wait(2)
        
        # Clean up EVERYTHING before moving to next section
        self.play(
            *[FadeOut(mob) for mob in [
                section_title,
                chart_title,
                axes,
                x_label,
                y_label,
                dots,
                line_graph,
                value_labels
            ]]
        )
        
        # Add extra wait to ensure complete cleanup
        self.wait(0.5)

    def show_tech_impact(self):
        # Clear any remaining objects first
        self.clear()
        
        # Create section title
        section_title = Text("Technology Impact on Economy", font_size=48)
        section_title.to_edge(UP, buff=0.5)
        
        # Create circular diagram for tech sectors
        sectors = ["AI", "Blockchain", "IoT", "Cloud", "5G"]
        circles = VGroup(*[
            Circle(radius=0.5).set_fill(color=BLUE, opacity=0.5)
            for _ in sectors
        ]).arrange_in_grid(rows=2, cols=3, buff=1)
        
        # Position circles below the title
        circles.next_to(section_title, DOWN, buff=1.5)
        
        labels = VGroup(*[
            Text(sector, font_size=24).move_to(circle)
            for sector, circle in zip(sectors, circles)
        ])
        
        # Animation sequence
        self.play(Write(section_title))
        self.play(Create(circles))
        self.play(Write(labels))
        
        # Pulse animation for each sector
        for circle in circles:
            self.play(
                circle.animate.scale(1.2),
                rate_func=there_and_back,
                run_time=0.5
            )
        
        # Clean up before next section
        self.play(
            *[FadeOut(mob) for mob in [section_title, circles, labels]]
        )
        self.wait(0.5)

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
