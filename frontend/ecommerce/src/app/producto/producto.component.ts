  import { Component, OnInit } from '@angular/core';
  import { InputNumberModule } from 'primeng/inputnumber';


  import { Producto } from 'src/models/producto.model'; 
  import { Categoria } from 'src/models/categoria.model'; 
  import { Proveedor } from 'src/models/proveedor.model'; 
  import { Negocio } from 'src/models/negocio.model'; 

  import { ApiServicio } from 'src/service/api-service';
  import { ConfirmationService, MessageService, ConfirmEventType } from 'primeng/api';


  @Component({
    selector: 'app-producto',
    templateUrl: './producto.component.html',
    styleUrls: ['./producto.component.css'],
    providers: [ConfirmationService, MessageService]
  })

  export class ProductoComponent implements OnInit {
    productos: Producto[];
    nuevoProducto: Producto = new Producto();
    esNuevoProducto: boolean;
    visible: boolean = false;

    intentoGuardar: boolean = false;

    categorias: Categoria[];
    categoriaSeleccionada: Categoria | null | undefined;
    proveedores: Proveedor[];
    proveedorSeleccionado: Proveedor | null | undefined;
    negocios: Negocio[];
    negocioSeleccionado: Negocio;

    constructor(private api:ApiServicio, private confirmationService: ConfirmationService, private messageService: MessageService){}

    ngOnInit() {
      this.obtenerProductos();

      this.obtenerCategorias();
      this.obtenerProveedores()
      this.obtenerNegocios();
      

    }

    showCreateBox() {
      this.esNuevoProducto = true;
      this.nuevoProducto = new Producto();
      this.visible = true;

      this.categoriaSeleccionada = new Categoria();
      this.proveedorSeleccionado = new Proveedor();
      this.negocioSeleccionado = new Negocio();

      this.nuevoProducto.descripcion = "";
    }

    showEditBox(producto: Producto) {
      this.esNuevoProducto = false;
      this.nuevoProducto = producto;
      this.visible = true;

      this.categoriaSeleccionada = producto.categoria_fk
        ? this.categorias.find(categoria => categoria.id === producto.categoria_fk)
        : null;

      this.proveedorSeleccionado = producto.proveedor_fk
        ? this.proveedores.find(proveedor => proveedor.id === producto.proveedor_fk)
        : null;

      this.negocioSeleccionado = this.negocios.find(negocio => negocio.id === producto.negocio_fk) || this.negocios[0];
  
    }

    grabarProducto() {
      
      if (this.categoriaSeleccionada === undefined || this.categoriaSeleccionada === null) {
        this.nuevoProducto.categoria_fk = null;
      } else {
        this.nuevoProducto.categoria_fk = this.categoriaSeleccionada.id;
      }

      if (this.proveedorSeleccionado === undefined || this.proveedorSeleccionado === null) {
        this.nuevoProducto.proveedor_fk = null;
      } else {
        this.nuevoProducto.proveedor_fk = this.proveedorSeleccionado.id;
      }

      this.nuevoProducto.negocio_nombre = this.negocioSeleccionado.nombre;
      this.nuevoProducto.negocio_fk = this.negocioSeleccionado.id;

      this.intentoGuardar = true;

      if (!this.nuevoProducto.nombre || !this.nuevoProducto.precio || !this.nuevoProducto.negocio_fk) {
        return;
      }

      
      if (this.esNuevoProducto) {

        this.api.post<Producto>('producto/', this.nuevoProducto).subscribe((respuesta) => {
          this.productos.push(respuesta); 
          this.obtenerProductos();
        });
      } else {


        this.api.put<Producto>(`producto/${this.nuevoProducto.id}`, this.nuevoProducto).subscribe(() => {
          this.obtenerProductos();
        });
      }

      console.log(this.nuevoProducto)
      
      this.visible = false;
      this.intentoGuardar = false;

    }

    obtenerProductos() {
      this.api.get<Producto[]>('producto').subscribe((respuesta) => {
        this.productos = respuesta; 
      });
    }

    crearProducto(nuevoProducto: Producto) {
      this.api.post<Producto>('producto/', nuevoProducto).subscribe((respuesta) => {
        this.obtenerProductos()
      });
    }
    
    eliminarProducto(productoId: number) {
      this.confirmationService.confirm({
        message: 'No podrás recuperar el producto una vez eliminado',
        header: '¿Estás seguro?',
        icon: 'pi pi-info-circle',
        acceptLabel: 'Sí',
        rejectLabel: 'No',
        acceptButtonStyleClass: 'p-button-danger', 
        rejectButtonStyleClass: 'p-button-secondary',
        acceptIcon: '',
        rejectIcon: '',
        accept: () => {
            this.messageService.add({ severity: 'success', summary: 'Producto eliminado', detail: 'El producto se eliminó correctamente' });

            this.api.delete<void>(`producto/${productoId}`).subscribe(() => {
              this.obtenerProductos()
            });

        },
        reject: (type: ConfirmEventType) => {
          switch (type) {
              case ConfirmEventType.REJECT:
                  this.messageService.add({ severity: 'info', summary: 'Eliminación cancelada', detail: 'No se eliminó el producto' });
                  break;
              case ConfirmEventType.CANCEL:
                  break;
          }
        }
      });    
    }

    obtenerCategorias() {
      this.api.get<Categoria[]>('categoria').subscribe((respuesta) => {
        this.categorias = respuesta; 
      });
    }

    obtenerProveedores() {
      this.api.get<Proveedor[]>('proveedor').subscribe((respuesta) => {
        this.proveedores = respuesta; 
      });
    }

    obtenerNegocios() {
      this.api.get<Negocio[]>('negocio').subscribe((respuesta) => {
        this.negocios = respuesta; 
      });
    }
  }
