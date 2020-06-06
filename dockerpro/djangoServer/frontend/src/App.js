import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Navbar, Nav, Card, Button, Form, Row, Col } from 'react-bootstrap'
import axios from 'axios'
import  FileDownload  from 'js-file-download';

class App extends React.Component {

  constructor(props){
    super(props)
    this.state = {
      "companyList" : [],
      "uploadCompany": "",
      "uploadFile": "",
      "downloadCompany" : ""
    }
  }

  getCompanyId = (name) => {
    return this.state.companyList.filter(item => item.name === name)[0].id
  }

  componentDidMount() {
    let that = this;
    axios.get('/companies')
    .then(function(res) {
      console.log("1", res)
      that.setState({"companyList": res.data.items, "uploadCompany": res.data.items[0].name, "downloadCompany": res.data.items[0].name})
    })
  }

  handleUploadCompanyChange = (event) => {
    this.setState({"uploadCompany": event.target.value})
  }

  handleUploadFileChange = (event) => {
    this.setState({"uploadFile": event.target.files[0]})
  }

  handleDownloadCompanyChange = (event) => {
    this.setState({"downloadCompany": event.target.value})
  }

  handleSubmitUpload = (event) => {
    event.preventDefault();
      const data = new FormData()
      data.append('file', this.state.uploadFile)
      axios.post('/impExpCompanyQrcode/'+this.getCompanyId(this.state.uploadCompany),data)
      .then(function(res) {
        console.log("1", res)
        alert(res.data.message)
        //that.setState({"companyList": res.data.items, "downloadCompany": res.data.items[0].name})
      })

  }

  handleSubmitDownload = (event) => {
    event.preventDefault();
    let that = this;
    console.log("2", this.state.downloadCompany)
    axios.get('/impExpCompanyQrcode/'+this.getCompanyId(this.state.downloadCompany))
    .then(function(res) {
      console.log("1", res)
      if(res.data.success){
        alert(res.data.message)
      } else if(res.data.success === false){
        alert(res.data.message)
      }else {
         FileDownload(res.data, that.state.downloadCompany + ".xlsx");
      }

      //that.setState({"companyList": res.data.items, "downloadCompany": res.data.items[0].name})
    })
  }



  render() {
    return (
      <div className="App">
        <Navbar bg="dark" variant="dark">
            <Navbar.Brand>Azure Press</Navbar.Brand>
        </Navbar>

        <div>
          <br/>
          <br/>
          <Card style={{ width: '75%', margin: 'auto' }}>
            <Card.Header>
              <Card.Title>Upload</Card.Title>
            </Card.Header>
            <Card.Body>
              <Form onSubmit={this.handleSubmitUpload}>
                <Row>
                  <Col>
                  <Row>
                  <Form.Group as={Col} controlId="downloadForm.companySelect">
                    <Form.Label>Select a Company:</Form.Label>
                    <Form.Control as="select" value={this.state.uploadCompany} onChange={this.handleUploadCompanyChange}>
                    {
                      this.state.companyList.map((item) => <option>{item.name}</option>)
                    }
                    </Form.Control>
                  </Form.Group>
                  <Form.Group as={Col} controlId="downloadForm.Select">
                    <Form.Label>File to be uploaded:</Form.Label>
                    <Form.Control  onChange={this.handleUploadFileChange} type="file" placeholder="Choose file" required multiple />
                  </Form.Group>
                  </Row>
                  </Col>
                  <Col>
                  <br/>
                  <Button variant="primary" type="submit">Upload</Button>
                  </Col>
                </Row>
              </Form>
            </Card.Body>
          </Card>
          <br/>
          <br/>
          <Card style={{ width: '75%', margin: 'auto' }}>
            <Card.Header>
              <Card.Title>Download</Card.Title>
            </Card.Header>
            <Card.Body>
                <Form onSubmit={this.handleSubmitDownload}>
                  <Row>
                    <Form.Group as={Col} controlId="downloadForm.companySelect">
                      <Form.Label>Select a Company:</Form.Label>
                      <Form.Control as="select" value={this.state.downloadCompany} onChange={this.handleDownloadCompanyChange}>
                      {
                        this.state.companyList.map((item) => <option>{item.name}</option>)
                      }
                      </Form.Control>
                    </Form.Group>
                    <Col>
                    <br/>
                    <Button variant="primary" type="submit">Download</Button>
                    </Col>
                  </Row>
                </Form>

            </Card.Body>
          </Card>
        </div>
      </div>
    );
  }
}

export default App;
