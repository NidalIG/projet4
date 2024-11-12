from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

if __name__ == "__main__":
    # Dessiner le graphique en ligne
    line_fig = draw_line_plot()
    
    # Dessiner le graphique en barres
    bar_fig = draw_bar_plot()
    
    # Dessiner les box plots
    box_fig = draw_box_plot()
