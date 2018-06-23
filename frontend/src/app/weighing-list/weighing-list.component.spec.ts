import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WeighingListComponent } from './weighing-list.component';

describe('WeighingListComponent', () => {
  let component: WeighingListComponent;
  let fixture: ComponentFixture<WeighingListComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WeighingListComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WeighingListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
