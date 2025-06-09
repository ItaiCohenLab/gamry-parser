import gamry_parser as parser
import random

file = "Z:\\Data\\2025-02-18-VoltageSpeedTest-200nm\\1-13-1-VoltageSpeedTestn1p2to0p6\\1-13-1-VoltageSpeedTestn1p2to0p6.DTA"
gp = parser.GamryParser()
gp.load(filename=file)
print("GamryParser() usage:")
print("experiment type: {}".format(gp.experiment_type))
print("loaded curves: {}".format(gp.curve_count))


print("showing curve #{}".format(0))
print(gp.curve(0))

ca = parser.RepeatingChronoAmperometry()
ca.load(filename=file)
print("RepeatingChronoAmperometry() usage:")
print(f"Current range mode: {ca.current_range_mode}")
print(f"Current range: {int(ca.current_range)}")
print(f"First Voltage Step: {ca.vstep1}")
print(f"Second Voltage Step: {ca.vstep2}")
print(f"First Voltage Step Duration: {ca.tstep1}")
print(f"Second Voltage Step Duration: {ca.tstep2}")
print(f"Number of cycles: {ca.cycle_count}")
print(f"current stability: {ca.current_stability}")
print(f"control_amp_speed: {ca.control_amp_speed}")
print(f"current_convention: {ca.current_convention}")
print(f"potentiostat: {ca.potentiostat}")
print(f"date: {ca.date}")
print(f"time: {ca.time()}")

