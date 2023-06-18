import processing.svg.*;

import grafica.*;
import java.util.ArrayList;

GPlot plot, plotMath;

void setup() {
  // Define the window size
  size(800, 650);

  // Load the cvs dataset. 
  // The file has the following format: 
  // country,income,health,population
  // Central African Republic,599,53.8,4900274
  // ...

  Table table = loadTable("data.csv", "header");

  // Save the data in one GPointsArray and calculate the point sizes
  GPointsArray points = new GPointsArray();
  float[] pointSizes = new float[table.getRowCount()];
  
  for (int row = 0; row < table.getRowCount(); row++) {
    String country = table.getString(row, "country");
    float income = table.getFloat(row, "income");
    float health = table.getFloat(row, "health");
    int population = table.getInt(row, "population");
    points.add(income, health, country);
    
    // The point area should be proportional to the country population
    // population = pi * sq(diameter/2) 
    pointSizes[row] = 2 * sqrt(population/(200000 * PI));
  }

  // Create the plot
  plot = new GPlot(this);
  plot.setPos(0, 0);
  plot.setDim(650, 200);
  plot.setTitleText("Função");
  plot.getXAxis().setAxisLabelText("Tempo");
  plot.getYAxis().setAxisLabelText("Amplitude");
  plot.setLogScale("x");
  plot.setPoints(points);
  plot.setPointSizes(pointSizes);
  plot.activatePointLabels();
  plot.activatePanning();
  plot.activateZooming(1.1, CENTER, CENTER);
  
  // Create new plot (Função matemática)
  float range = 2 * PI * 4;
  float increment = 0.01;
  
  GPointsArray pointsMath = new GPointsArray();
  
  for (float x = 0; x < range; x = x + increment) {
    pointsMath.add(x, sin(x), str(sin(x)));
  }
  
  plotMath = new GPlot(this);
  plotMath.setPos(0, 300);
  plotMath.setDim(650, 250);
  plotMath.setTitleText("Função");
  plotMath.getXAxis().setAxisLabelText("X");
  plotMath.getYAxis().setAxisLabelText("Y");
  
  plotMath.setPoints(pointsMath);
  plotMath.activatePanning();
  plotMath.activateZooming(1.1, CENTER, CENTER, GPlot.CTRLMOD, GPlot.CTRLMOD);
  
  plotMath.setLineColor(color(200, 200, 255));
}

void draw() {
  // Clean the screen
  background(255);

  // Draw the plot  
  plot.beginDraw();
    plot.drawBox();
    plot.drawXAxis();
    plot.drawYAxis();
    plot.drawTitle();
    plot.drawGridLines(GPlot.BOTH);
    plot.drawPoints();
    plot.drawLabels();
  plot.endDraw();
  
  // Draw the another plot
  plotMath.beginDraw();
    plotMath.drawBox();
    plotMath.drawXAxis();
    plotMath.drawYAxis();
    plotMath.drawTitle();
    
    plotMath.drawLines();
    plotMath.drawLabels();
    
    plotMath.drawLine(0,0,100,1);
    plotMath.drawLine(new GPoint(0, -10), new GPoint(0, 10),100,1);
    
    plotMath.drawXAxis();
    plotMath.drawYAxis();
  plotMath.endDraw();
}
