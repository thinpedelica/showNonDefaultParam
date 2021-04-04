import hou

for pane in hou.ui.curDesktop().panes():
  for tab in pane.tabs():
    if tab.type() == hou.paneTabType.Parm:
      if tab.filterEnabled():
        tab.setFilterEnabled(False)
      else:
        tab.setFilterEnabled(True)
        # set filter Non-Default 
        ## The value of enum is sliding by one.(maybe Houdini's bag at houdini 18.5.499)
        tab.setFilterMode(hou.parmFilterMode.GraphSelectedParms)
