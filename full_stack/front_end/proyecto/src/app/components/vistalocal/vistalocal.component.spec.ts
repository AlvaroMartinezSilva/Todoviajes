import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VistalocalComponent } from './vistalocal.component';

describe('VistalocalComponent', () => {
  let component: VistalocalComponent;
  let fixture: ComponentFixture<VistalocalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VistalocalComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VistalocalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
