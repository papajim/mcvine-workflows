<?xml version="1.0"?>
<!DOCTYPE inventory>

<inventory>

    <component name="simapp1">
        <property name="sequence">['source', 'monitor']</property>
        <facility name="source">sources/Source_simple</facility>
        <facility name="monitor">monitors/E_monitor</facility>
        <property name="multiple-scattering">False</property>
        <property name="output-dir">out</property>
        <property name="overwrite-datafiles">False</property>
        <property name="launcher">mpirun</property>

        <component name="source">
            <property name="name">source_simple</property>
            <property name="height">0.0</property>
            <property name="width">0.0</property>
            <property name="radius">0.05</property>
            <property name="xw">0.1</property>
            <property name="yh">0.1</property>
            <property name="dist">10.0</property>
            <property name="E0">60.0</property>
            <property name="dE">10.0</property>
            <property name="dLambda">0.0</property>
            <property name="Lambda0">0.0</property>
            <property name="gauss">0.0</property>
            <property name="flux">1.0</property>
        </component>


        <component name="monitor">
            <property name="name">e_monitor</property>
            <property name="xwidth">0.2</property>
            <property name="yheight">0.2</property>
            <property name="xmin">0.0</property>
            <property name="xmax">0.0</property>
            <property name="ymin">0.0</property>
            <property name="ymax">0.0</property>
            <property name="Emin">30.0</property>
            <property name="Emax">90.0</property>
            <property name="nchan">20</property>
            <property name="filename">IE.dat</property>
        </component>


        <component name="geometer">
            <property name="source">((0, 0, 0), (0, 0, 0))</property>
            <property name="monitor">((0, 0, 10), (0, 0, 0))</property>
        </component>


        <component name="mpirun">
            <property name="command">mpirun</property>
            <property name="python-mpi">`which python`</property>
            <property name="nodelist">[]</property>
            <property name="dry">False</property>
            <property name="extra"></property>
            <property name="debug">False</property>
            <property name="nodes-opt">-np</property>
            <property name="nodes">0</property>
        </component>

    </component>

</inventory>

