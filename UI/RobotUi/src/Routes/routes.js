import React from 'react';
import { BellOutlined, CodeOutlined, ControlOutlined, FundOutlined, SettingOutlined } from '@ant-design/icons';
import { Stats } from '../Pages/Stats';


export const routes = [
  {
    index: true,
    path: '',
    element: <Stats/>,
    icon: <FundOutlined />,
    label: 'Stats',
  },
  {
    path: 'motors',
    element: <>Motors Page placeholder</>,
    icon: <BellOutlined />,
    label: 'Motors'
  },
  {
    path: 'servos',
    element: <>Servos Page placeholder</>,
    icon: <BellOutlined />,
    label: 'Servos'
  }, 
  {
    path: 'joystick',
    element: <>Joystick Page placeholder</>,
    icon: <ControlOutlined />,
    label: 'Joystick'
  },
  {
    path: 'spi_terminal',
    element: <>SPI Terminal Page placeholder</>,
    icon: <CodeOutlined />,
    label: 'SPI Terminal'
  },
  {
    path: 'ctd_terminal',
    element: <>CTD Terminal Page placeholder</>,
    icon: <CodeOutlined />,
    label: 'CTD Terminal'
  },
  {
    path: 'settings',
    element: <>Settings Page placeholder</>,
    icon: <SettingOutlined />,
    label: 'DBUI Settings'
  },
  

];


// const menu = [
//   {
//       key: '0',
//       icon: <FundOutlined />,
//       label: "Stats"
//   },
//   {
//       key: '1',
//       icon: <BellOutlined />,
//       label: "Motors"

//   },
//   {
//       key: '2',
//       icon: <BellOutlined />,
//       label: "Servos"
//   },
//   {
//       key: '3',
//       icon: <ControlOutlined />,
//       label: "Joystick"
//   },
//   {
//       key: '4',
//       icon: <CodeOutlined />,
//       label: "SPI Terminal"
//   },
//   {
//       key: '5',
//       icon: <CodeOutlined />,
//       label: "CTD Terminal"
//   },
//   {
//       key: '6',
//       icon: <CodeOutlined />,
//       label: "Serial Terminal"
//   },
//   {
//       key: '8',
//       icon: <SettingOutlined />,
//       label: "Settings"
//   }
// ];