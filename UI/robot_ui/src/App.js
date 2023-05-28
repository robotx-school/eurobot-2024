import { BellOutlined, CodeOutlined, ControlOutlined, FundOutlined } from '@ant-design/icons';
import { Liquid } from '@ant-design/plots';
import { Layout, Menu, Space, theme, Typography } from 'antd';
import React from 'react';
import './App.css';

const { Content, Sider } = Layout;
const { Text } = Typography;

const UsageLiquid = ({ percent, title, color }) => (
  <Space direction='vertical' align='center'>
    <Liquid {...{
      color: color,
      width: 200,
      height: 200,
      percent: percent,
      outline: {
        border: 4,
        distance: 4,
      },
      wave: {
        length: 128,
      }
    }} />
    <Text strong>{title}</Text>
  </Space>
)

const App = () => {
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
    }
  ];
  return (
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
              background: colorBgContainer,
            }}
          >
            <h3>RPi Statistic</h3>
            <Space direction='horizontal' size='large' style={{ width: '100%', justifyContent: 'center' }}>
              <UsageLiquid percent={0.9} color={"#8BC34A"} title={"CPU"} />
              <UsageLiquid percent={0.6} color={"#4ac387"} title={"RAM"} />
              <UsageLiquid percent={0.3} color={"#c34a4a"} title={"SD"} />
            </Space>

          </div>
        </Content>

      </Layout>
    </Layout>
  );
};
export default App;