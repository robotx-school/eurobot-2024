import { BellOutlined, CodeOutlined, ControlOutlined, FundOutlined } from '@ant-design/icons';
import { Liquid, Bullet } from '@ant-design/plots';
import { Layout, Menu, Space, theme, Typography, Table, ConfigProvider } from 'antd';
import React from 'react';
import './App.css';

const { Content, Sider } = Layout;
const { Text, Title } = Typography;

const UsageLiquid = ({ percent, title, color, theme }) => (
  <Space direction='vertical' align='center'>
    <Liquid {...{
      color: color,
      width: 200,
      height: 200,
      percent: percent,
      statistic: {
        content: {
          style: {
            fill: "#fff" ? theme === "dark" : "#000"
          },
        },
      },
      outline: {
        border: 4,
        distance: 2,
      },
      wave: {
        length: 128,
      }
    }} />
    <Text strong>{title}</Text>
  </Space>
);
const TemperatureBullet = ({ current }) => {
  const data = [
    {
      title: '',
      ranges: [45, 70, 85],
      measures: [current],
      target: 85,
    },
  ];
  const config = {
    data,
    measureField: 'measures',
    height: 10,
    padding: 10,
    rangeField: 'ranges',
    targetField: 'target',
    xField: 'title',
    color: {
      range: ['#bfeec8', '#FFe0b0', '#FFbcb8'],
      measure: '#5B8FF9',
      target: '#FFbcb8',
    },
    xAxis: {
      line: null,
    },
    yAxis: false,
    label: {
      target: true,
    },
  };
  return <Bullet {...config} style={{ marginBottom: 40, marginTop: 40 }} />;
}

const App = () => {
  let color_theme = "light";
  const {
    token: { colorBgContainer },
  } = theme.useToken();
  const menu = [
    {
      key: '0',
      icon: <FundOutlined />,
      label: "Stats"
    },
    {
      key: '1',
      icon: <BellOutlined />,
      label: "Motors"

    },
    {
      key: '2',
      icon: <BellOutlined />,
      label: "Servos"
    },
    {
      key: '3',
      icon: <ControlOutlined />,
      label: "Joystick"
    },
    {
      key: '4',
      icon: <CodeOutlined />,
      label: "SPI Terminal"
    },
    {
      key: '5',
      icon: <CodeOutlined />,
      label: "CTD Terminal"
    },
    {
      key: '6',
      icon: <CodeOutlined />,
      label: "Serial Terminal"
    }
  ];
  const RpiTableData = [
    {
      key: 'local_ip',
      item: 'Local IP',
      value: '192.168.115.200'
    },
    {
      key: 'auth_data',
      item: 'Auth data',
      value: 'pi:pi'
    },
    {
      key: 'gl_git',
      item: 'High-Level git hash',
      value: '97b24441c6ae86d189d4cba92cadcaf976676cfe'
    },
    {
      key: 'ros_status',
      item: 'ROS reports',
      value: 'roscore up; noetic 1.15.14'
    },
    {
      key: 'll_connection',
      item: 'Low-Level SPI connection',
      value: 'Healthy (init packet control sum based check)'
    },

  ];

  const RpiTableColumns = [
    {
      title: 'Item',
      dataIndex: 'item',
      key: 'item',
      render: (_, record) => (
        <Text strong>{record.item}</Text>
      )
    },
    {
      title: 'Value',
      dataIndex: 'value',
      key: 'value',
    },
  ];


  return (
    <ConfigProvider
      theme={{
        algorithm: theme.darkAlgorithm ? color_theme === "dark" : color_theme.defaultSelectedKeys
      }}
    >
      <Layout>
        <Sider
          className="main-slider"
          breakpoint="lg"
          collapsedWidth="0"
          style={{
            height: '100vh',
          }}

        >
          <div className="logo" />
          <Menu
            theme="dark"
            mode="inline"
            defaultSelectedKeys={['0']}
            items={menu}
          />
        </Sider>
        <Layout>

          <Content
            style={{
              margin: '24px 16px 0',
            }}
          >
            <div
              style={{
                padding: 24,
                minHeight: 360,
                backgroundColor: "#fff" ? color_theme === "dark" : "#000",
              }}
            >
              <Title level={3}>RPi Statistic</Title>
              <Space direction='horizontal' size='large' style={{ width: '100%', justifyContent: 'center', marginBottom: 40 }}>
                <UsageLiquid percent={0.9} color={"#8BC34A"} title={"CPU"} theme={color_theme} />
                <UsageLiquid percent={0.6} color={"#4ac387"} title={"RAM"} theme={color_theme} />
                <UsageLiquid percent={0.3} color={"#c34a4a"} title={"SD"} theme={color_theme} />
              </Space>
              <Text strong>CPU temperature</Text>
              <TemperatureBullet current={40} />
              <Table dataSource={RpiTableData} columns={RpiTableColumns} />
            </div>

            {/* <div
            style={{
              padding: 24,
              minHeight: 360,
              background: colorBgContainer,
              marginTop: 20
            }}
          >
            <h3>Motors</h3>
            <Space direction='horizontal' size='large' style={{ width: '100%', justifyContent: 'center' }}>
              <UsageLiquid percent={0.9} color={"#8BC34A"} title={"CPU"} />
              <UsageLiquid percent={0.6} color={"#4ac387"} title={"RAM"} />
              <UsageLiquid percent={0.3} color={"#c34a4a"} title={"SD"} />
            </Space>

          </div> */}
          </Content>

        </Layout>
      </Layout>
    </ConfigProvider>
  );
};
export default App;