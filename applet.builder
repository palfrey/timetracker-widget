<?xml version="1.0"?>
<interface>
  <requires lib="gtk+" version="2.16"/>
  <!-- interface-naming-policy project-wide -->
  <object class="GtkDialog" id="dlgChooseAction">
    <property name="border_width">5</property>
    <property name="title" translatable="yes">Choose action</property>
    <property name="type_hint">normal</property>
    <child internal-child="vbox">
      <object class="GtkVBox" id="dialog-vbox1">
        <property name="visible">True</property>
        <property name="orientation">vertical</property>
        <property name="spacing">2</property>
        <child>
          <object class="GtkHBox" id="hbox1">
            <property name="visible">True</property>
            <child>
              <object class="GtkVBox" id="vbox2">
                <property name="height_request">40</property>
                <property name="visible">True</property>
                <property name="orientation">vertical</property>
                <child>
                  <object class="GtkLabel" id="label1">
                    <property name="height_request">30</property>
                    <property name="visible">True</property>
                    <property name="label" translatable="yes">Project</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkComboBoxText" id="cmbProject">
                    <property name="height_request">30</property>
                    <property name="visible">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkVBox" id="vbox3">
                <property name="visible">True</property>
                <property name="orientation">vertical</property>
                <child>
                  <object class="GtkLabel" id="label2">
                    <property name="height_request">30</property>
                    <property name="visible">True</property>
                    <property name="label" translatable="yes">Activity</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkComboBoxText" id="cmbActivity">
                    <property name="height_request">30</property>
                    <property name="visible">True</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkVBox" id="vbox4">
                <property name="visible">True</property>
                <property name="orientation">vertical</property>
                <child>
                  <object class="GtkLabel" id="label3">
                    <property name="height_request">30</property>
                    <property name="visible">True</property>
                    <property name="label" translatable="yes">Bug</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="entBug">
                    <property name="width_request">80</property>
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="invisible_char">&#x25CF;</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="fill">False</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">2</property>
              </packing>
            </child>
            <child>
              <object class="GtkVBox" id="vbox5">
                <property name="visible">True</property>
                <property name="orientation">vertical</property>
                <child>
                  <object class="GtkLabel" id="label4">
                    <property name="height_request">30</property>
                    <property name="visible">True</property>
                    <property name="label" translatable="yes">Description</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="position">0</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkEntry" id="entDescription">
                    <property name="visible">True</property>
                    <property name="can_focus">True</property>
                    <property name="invisible_char">&#x25CF;</property>
                  </object>
                  <packing>
                    <property name="expand">False</property>
                    <property name="position">1</property>
                  </packing>
                </child>
              </object>
              <packing>
                <property name="position">3</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="position">1</property>
          </packing>
        </child>
        <child internal-child="action_area">
          <object class="GtkHButtonBox" id="dialog-action_area1">
            <property name="visible">True</property>
            <property name="layout_style">end</property>
            <child>
              <object class="GtkButton" id="button1">
                <property name="label">gtk-ok</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="button2">
                <property name="label">gtk-cancel</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">1</property>
              </packing>
            </child>
            <child>
              <object class="GtkButton" id="button3">
                <property name="label" translatable="yes">IDLE</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">2</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="pack_type">end</property>
            <property name="position">0</property>
          </packing>
        </child>
      </object>
    </child>
    <action-widgets>
      <action-widget response="1">button1</action-widget>
      <action-widget response="2">button2</action-widget>
      <action-widget response="3">button3</action-widget>
    </action-widgets>
  </object>
  <object class="GtkDialog" id="dialog1">
    <property name="border_width">5</property>
    <property name="type_hint">normal</property>
    <child internal-child="vbox">
      <object class="GtkVBox" id="dlgUsers">
        <property name="visible">True</property>
        <property name="orientation">vertical</property>
        <property name="spacing">2</property>
        <child>
          <placeholder/>
        </child>
        <child internal-child="action_area">
          <object class="GtkHButtonBox" id="dialog-action_area2">
            <property name="visible">True</property>
            <property name="layout_style">end</property>
            <child>
              <object class="GtkButton" id="button4">
                <property name="label">gtk-ok</property>
                <property name="visible">True</property>
                <property name="can_focus">True</property>
                <property name="receives_default">True</property>
                <property name="use_stock">True</property>
              </object>
              <packing>
                <property name="expand">False</property>
                <property name="fill">False</property>
                <property name="position">0</property>
              </packing>
            </child>
          </object>
          <packing>
            <property name="expand">False</property>
            <property name="pack_type">end</property>
            <property name="position">0</property>
          </packing>
        </child>
      </object>
    </child>
    <action-widgets>
      <action-widget response="0">button4</action-widget>
    </action-widgets>
  </object>
</interface>
