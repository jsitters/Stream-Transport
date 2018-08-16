Constant Volume:
##loop through segments to calculate outflow and parameters for each time step.
for t in range((len(time_s))):
    for i in range(nsegments):
        Q_out.iloc[t, i + 2] = Q_out.iloc[t, i + 1]  # + tributary flow
        HP_depth.iloc[t, i+2] = (model_segs['init_depth'][i]) ## This is the difference between Flow Routing and Stream Routing
        if model_segs['ChanGeom'][i] == 'tz':
            HP_areaC.iloc[t, i+2] = model_segs['bot_width'][i] * HP_depth.iloc[t, i+2] + model_segs['z_slope'][i] * HP_depth.iloc[t, i+2] ** 2
        elif model_segs['ChanGeom'][i] == 'r':
            HP_areaC.iloc[t, i+2] = model_segs['bot_width'][i] * HP_depth.iloc[t, i+2]
        elif model_segs['ChanGeom'][i] == 't':
            HP_areaC.iloc[t, i+2] = model_segs['z_slope'][i] * HP_depth.iloc[t, i+2] ** 2
        HP_vel.iloc[t, i+2] = Q_out.iloc[t, i + 2] / HP_areaC.iloc[t, i+2]
        HP_vol.iloc[t, i+2] = model_segs['length'][i] * HP_areaC.iloc[t, i+2]
        HP_rt.iloc[t, i+2] = HP_vol.iloc[t, i+2] / Q_out.iloc[t, i + 2] / 24 / 60 / 60
        
Changing Volume:	
##loop through segments to calculate outflow and parameters for each time step.
for t in range((len(time_s))):
    for i in range(nsegments):
        Q_out.iloc[t, i + 2] = Q_out.iloc[t, i + 1]  # + tributary flow
        HP_depth.iloc[t, i+2] = 10**(model_segs['depth_intercept'][i])*Q_out.iloc[t, i + 2]**model_segs['depth_exp'][i] ## This is the only difference between Flow Routing and Stream Routing
        if model_segs['ChanGeom'][i] == 'tz':
            HP_areaC.iloc[t, i+2] = model_segs['bot_width'][i] * HP_depth.iloc[t, i+2] + model_segs['z_slope'][i] * HP_depth.iloc[t, i+2] ** 2
        elif model_segs['ChanGeom'][i] == 'r':
            HP_areaC.iloc[t, i+2] = model_segs['bot_width'][i] * HP_depth.iloc[t, i+2]
        elif model_segs['ChanGeom'][i] == 't':
            HP_areaC.iloc[t, i+2] = model_segs['z_slope'][i] * HP_depth.iloc[t, i+2] ** 2
        HP_vel.iloc[t, i+2] = Q_out.iloc[t, i + 2] / HP_areaC.iloc[t, i+2]
        HP_vol.iloc[t, i+2] = model_segs['length'][i] * HP_areaC.iloc[t, i+2]
        HP_rt.iloc[t, i+2] = HP_vol.iloc[t, i+2] / Q_out.iloc[t, i + 2] / 24 / 60 / 60
