import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use("SVG")
import matplotlib.pyplot as plt


def create_portfolio_risk_data(num_assets, num_risk_factors, num_time_periods):
  """
  Simulates portfolio risk data with labels.

  Args:
      num_assets: Number of assets in the portfolio.
      num_risk_factors: Number of risk factors considered.
      num_time_periods: Number of time periods for data.

  Returns:
      A tuple containing:
          data: A structured NumPy array holding data and labels.
          asset_labels: List of asset labels.
          risk_factor_labels: List of risk factor labels.
          time_period_labels: List of time period labels.
  """

  # Define data structure
  data_dtype = [('asset', 'S10'), ('risk_factor', 'S20'), ('time_period', int), ('value', float)]
  data = np.zeros((num_assets, num_risk_factors, num_time_periods), dtype=data_dtype)

  # Simulate some data (replace with actual data and decomposition)
  for i in range(num_assets):
    for j in range(num_risk_factors):
      for k in range(num_time_periods):
        data[i, j, k]['value'] = i * j * k
        data[i, j, k]['asset'] = f"Asset {i+1}"
        data[i, j, k]['risk_factor'] = f"Risk Factor {j+1}"
        data[i, j, k]['time_period'] = 2022 + k

  # Extract labels
  asset_labels = data['asset']
  risk_factor_labels = data['risk_factor']
  time_period_labels = data['time_period']

  return data, asset_labels, risk_factor_labels, time_period_labels


def visualize_portfolio_risk(data, asset_labels, risk_factor_labels, time_period_labels):
  """
  Visualizes portfolio risk data using a 3D wireframe plot.

  Args:
      data: A NumPy array containing the risk data.
      asset_labels: List of asset labels.
      risk_factor_labels: List of risk factor labels.
      time_period_labels: List of time period labels.
  """

  # Reshape data for plotting
  data_values = data['value'].reshape((len(asset_labels), len(risk_factor_labels), len(time_period_labels)))

  # Create a 3D wireframe plot
  fig = plt.figure(figsize=(10, 6))
  ax = fig.add_subplot(111, projection='3d')

  # Plot the wireframe with custom labels
  X, Y = np.meshgrid(range(len(asset_labels)), range(len(risk_factor_labels)))
  ax.plot_wireframe(X, Y, data_values, color='blue', label='Portfolio Risk')
  ax.set_xticks(range(len(asset_labels)))
  ax.set_yticks(range(len(risk_factor_labels)))
  ax.set_xticklabels(asset_labels, rotation=45, ha='right')  # Rotate and align asset labels
  ax.set_yticklabels(risk_factor_labels)
  ax.set_zlabel('Time Period (' + ', '.join(str(p) for p in time_period_labels) + ')')
  ax.set_xlabel('Assets')
  ax.set_ylabel('Risk Factors')
  ax.set_title('Portfolio Risk Data (Example)')
  ax.legend()

  # Customize plot options (optional)
  ax.set_aspect('equal')  # Set equal aspect ratio for better visualization

  plt.show()


def execute_portfolio_risk_visualization():
  """
  Executes the portfolio risk data generation and visualization process.
  """

  # Define data dimensions
  num_assets = 3
  num_risk_factors = 2
  num_time_periods = 2

  # Generate data and labels
  data, asset_labels, risk_factor_labels, time_period_labels = create_portfolio_risk_data(num_assets, num_risk_factors, num_time_periods)
