import { Component, OnInit } from '@angular/core';
import { HttpService } from '../http.service';
import { FormGroup, FormBuilder, Validators} from '@angular/forms';

@Component({
  selector: 'app-converter',
  templateUrl: './converter.component.html',
  styleUrls: ['./converter.component.scss'],
  providers: [HttpService]
})
export class ConverterComponent implements OnInit {
  input: any = ''
  output: any = ''
  converterForm: FormGroup;

  constructor(private fb: FormBuilder, private httpService: HttpService){}

  ngOnInit() {
    this.initForm()
  }

  getIntFromRomanResult() {
    let inputNum = this.converterForm.value["inputNumber"];
    if(isNaN(inputNum)){
      this.httpService.postRoman(inputNum).subscribe(res => {
        this.converterForm.patchValue({outputNumber: res.body["int_number"]})
      })
    } else {
      this.httpService.postInt(+inputNum).subscribe(res => {
        this.converterForm.patchValue({outputNumber: res.body["roman_number"]})
      })
    }
    
  }

  initForm() {
    this.converterForm = this.fb.group({
      inputNumber: ['', [
        Validators.required,
        Validators.pattern('^([mdclxvi]+|[0-9]+)$')
       ]],
      outputNumber: ['']
    })
  }

}

// import { Component, OnInit } from '@angular/core';
// import { Http } from '@angular/http';

// @Component({
//   selector: 'app-show-data',
//   templateUrl: './show-data.component.html',
//   styleUrls: ['./show-data.component.css']
// })
// export class ShowDataComponent implements OnInit {
//   data: any
//   private req: any
//   url: string = '/getData/'

//   constructor(private http:Http) { }

//   ngOnInit() {
//   	this.req = this.http.get(this.url).subscribe(data => {
//       console.log(data.json())
//       this.data = data.json() as [any]
//     })
//   }

//   ngOnDestroy(){
//     this.req.unsubscribe()
//   }

// }